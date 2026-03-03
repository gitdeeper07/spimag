"""XGBoost + SHAP 8-parameter classifier."""

import xgboost as xgb
import shap
import numpy as np
from typing import Optional, Dict, List, Tuple


class XGBoostSMNIClassifier:
    """XGBoost classifier with SHAP attribution."""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.model = None
        self.explainer = None
        self.feature_names = [
            'S_yield', 'ΔE_zeeman', 'Γ_coh', 'θ_inc',
            'χ_para', 'P_singlet', 'Ω_dipole', 'V_nav'
        ]
        
    def train(self, X: np.ndarray, y: np.ndarray):
        """Train XGBoost model."""
        self.model = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8
        )
        self.model.fit(X, y)
        self.explainer = shap.TreeExplainer(self.model)
        
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict SMNI class."""
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict(X)
    
    def explain(self, X: np.ndarray) -> Dict:
        """Generate SHAP attribution."""
        if self.explainer is None:
            raise ValueError("Explainer not initialized")
        
        shap_values = self.explainer.shap_values(X)
        
        return {
            'shap_values': shap_values,
            'feature_names': self.feature_names,
            'base_value': self.explainer.expected_value
        }
