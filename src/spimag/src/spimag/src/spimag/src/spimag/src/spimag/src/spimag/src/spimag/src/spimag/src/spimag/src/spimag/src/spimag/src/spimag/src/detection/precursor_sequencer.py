"""Parameter sequence analysis for precursor detection."""

import numpy as np
from typing import List, Dict, Optional, Tuple
from collections import deque


class PrecursorSequencer:
    """Track parameter sequences preceding events."""
    
    def __init__(self, window_days: int = 60):
        self.window_days = window_days
        self.sequence_history = deque(maxlen=window_days)
        
    def add_observation(self, params: Dict[str, float], timestamp: float):
        """Add parameter observation."""
        self.sequence_history.append({
            'time': timestamp,
            'params': params.copy()
        })
        
    def detect_sequence(self) -> Optional[Dict]:
        """Detect characteristic precursor sequence."""
        if len(self.sequence_history) < 7:
            return None
            
        # Look for: He_ratio rise → Γ_geo increase → Rn_pulse spike
        he_ratio_trend = self._compute_trend('He_ratio', window=14)
        gamma_trend = self._compute_trend('Γ_geo', window=7)
        rn_spike = self._detect_spike('P_singlet', threshold=2.0)
        
        if he_ratio_trend > 0.1 and gamma_trend > 0.05 and rn_spike:
            return {
                'detected': True,
                'lead_time_days': self._estimate_lead_time(),
                'confidence': min(he_ratio_trend + gamma_trend + rn_spike, 1.0)
            }
        
        return {'detected': False}
    
    def _compute_trend(self, param: str, window: int) -> float:
        """Compute trend for a parameter."""
        if len(self.sequence_history) < window:
            return 0.0
            
        values = [obs['params'].get(param, 0) 
                 for obs in list(self.sequence_history)[-window:]]
        
        if not values or len(values) < 2:
            return 0.0
            
        # Simple linear trend
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]
        
        return max(0, slope)
    
    def _detect_spike(self, param: str, threshold: float = 2.0) -> bool:
        """Detect if current value is a spike."""
        if len(self.sequence_history) < 10:
            return False
            
        values = [obs['params'].get(param, 0) 
                 for obs in list(self.sequence_history)[:-1]]
        
        if not values:
            return False
            
        mean = np.mean(values)
        std = np.std(values)
        current = self.sequence_history[-1]['params'].get(param, 0)
        
        return current > mean + threshold * std
    
    def _estimate_lead_time(self) -> float:
        """Estimate lead time to event in days."""
        # Simplified estimation
        return 14.0  # 14 days default
