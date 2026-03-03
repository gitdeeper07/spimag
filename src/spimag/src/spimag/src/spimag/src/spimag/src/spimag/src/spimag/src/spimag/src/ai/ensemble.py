"""Ensemble fusion for SMNI prediction."""

import numpy as np
from typing import Dict, List, Optional, Tuple
import torch
import xgboost as xgb


class SMNIEnsemble:
    """Ensemble model combining LSTM, XGBoost, CNN, and PI-QNN."""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.weights = {
            'lstm': 0.30,
            'xgboost': 0.30,
            'cnn': 0.20,
            'pi_qnn': 0.20
        }
        self.models = {}
        
    def add_model(self, name: str, model):
        """Add a model to the ensemble."""
        self.models[name] = model
        
    def predict(self, data: Dict) -> Tuple[float, str, Dict]:
        """Predict SMNI score and alert level."""
        predictions = {}
        
        for name, model in self.models.items():
            if name == 'lstm' and 'timeseries' in data:
                # LSTM prediction
                pred = model.predict(data['timeseries'])
                predictions[name] = pred.item() if hasattr(pred, 'item') else pred
                
            elif name == 'xgboost' and 'parameters' in data:
                # XGBoost prediction
                pred = model.predict(data['parameters'].reshape(1, -1))
                predictions[name] = pred[0]
                
            elif name == 'cnn' and 'spatial' in data:
                # CNN prediction
                pred = model.predict(data['spatial'])
                predictions[name] = pred.item() if hasattr(pred, 'item') else pred
                
            elif name == 'pi_qnn' and 'quantum' in data:
                # PI-QNN prediction
                pred = model.predict(data['quantum'])
                predictions[name] = pred.item() if hasattr(pred, 'item') else pred
        
        # Weighted ensemble prediction
        smni_score = 0.0
        total_weight = 0.0
        
        for name, pred in predictions.items():
            weight = self.weights.get(name, 0.0)
            smni_score += weight * pred
            total_weight += weight
        
        if total_weight > 0:
            smni_score /= total_weight
        
        # Determine alert level
        alert_level = self._get_alert_level(smni_score)
        
        return smni_score, alert_level, predictions
    
    def _get_alert_level(self, smni: float) -> str:
        """Convert SMNI score to alert level."""
        if smni > 0.88:
            return "OPTIMAL"
        elif smni > 0.72:
            return "GOOD"
        elif smni > 0.55:
            return "MODERATE"
        elif smni > 0.38:
            return "MARGINAL"
        else:
            return "DYSFUNCTIONAL"
