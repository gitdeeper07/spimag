"""CNN for retinal spatial pattern recognition."""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple


class CNNSpatialPattern(nn.Module):
    """CNN for detecting spatial patterns in retinal cryptochrome array."""
    
    def __init__(self, input_channels: int = 1, num_classes: int = 5):
        super().__init__()
        
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Calculate flattened size after convolutions
        self.flattened_size = 64 * 8 * 8  # Assuming input 32x32
        
        self.fc1 = nn.Linear(self.flattened_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, self.flattened_size)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
    
    def predict(self, x):
        """Predict spatial pattern class."""
        self.eval()
        with torch.no_grad():
            return self.forward(x)
