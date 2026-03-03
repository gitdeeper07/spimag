"""SHAP attribution narrative generator."""

from typing import Dict, List, Optional
import numpy as np


class SHAPReporter:
    """Generate human-readable SHAP attribution reports."""
    
    def __init__(self):
        self.param_names = {
            'S_yield': 'Spin Quantum Yield',
            'ΔE_zeeman': 'Zeeman Energy Splitting',
            'Γ_coh': 'Quantum Coherence Lifetime',
            'θ_inc': 'Magnetic Inclination Sensitivity',
            'χ_para': 'Paramagnetic Susceptibility',
            'P_singlet': 'Singlet-Triplet Probability',
            'Ω_dipole': 'Dipolar Coupling Tensor',
            'V_nav': 'Navigational Vector Precision'
        }
        
    def generate_report(self, shap_values: np.ndarray, 
                        feature_names: List[str],
                        base_value: float,
                        prediction: float) -> str:
        """Generate narrative report from SHAP values."""
        lines = []
        lines.append("=" * 60)
        lines.append("SMNI SHAP ATTRIBUTION REPORT")
        lines.append("=" * 60)
        lines.append(f"\nBase value: {base_value:.3f}")
        lines.append(f"Prediction: {prediction:.3f}")
        lines.append(f"Difference: {prediction - base_value:.3f}")
        lines.append("\nParameter Contributions:")
        
        # Sort by absolute SHAP value
        indices = np.argsort(np.abs(shap_values))[::-1]
        
        for i in indices:
            param = feature_names[i]
            shap_val = shap_values[i]
            param_name = self.param_names.get(param, param)
            
            if abs(shap_val) > 0.01:
                direction = "increased" if shap_val > 0 else "decreased"
                lines.append(f"  • {param_name}: {shap_val:+.3f} "
                           f"({direction} prediction)")
        
        lines.append("\n" + "=" * 60)
        return "\n".join(lines)
