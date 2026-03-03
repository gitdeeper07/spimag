"""LSTM for temporal spin dynamics prediction."""

import torch
import torch.nn as nn
from typing import Optional, Dict


class LSTMSpinDetector(nn.Module):
    """LSTM model for detecting spin dynamics anomalies."""
    
    def __init__(self, input_dim: int = 10, hidden_dim: int = 64, 
                 num_layers: int = 2, output_dim: int = 1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        last_time_step = lstm_out[:, -1, :]
        output = self.fc(last_time_step)
        return output
    
    def predict(self, x):
        """Predict spin coherence evolution."""
        self.eval()
        with torch.no_grad():
            return self.forward(x)
