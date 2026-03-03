"""Background modeling and baseline removal."""

import numpy as np
from typing import Optional, Tuple
from scipy import signal


class BackgroundModeling:
    """Background signal modeling and removal."""
    
    def __init__(self, window_days: int = 30):
        self.window_days = window_days
        
    def rolling_median(self, data: np.ndarray, time: np.ndarray) -> np.ndarray:
        """Calculate rolling median background."""
        background = np.zeros_like(data)
        
        for i in range(len(data)):
            # Find indices within window
            start = max(0, i - self.window_days)
            end = min(len(data), i + self.window_days)
            background[i] = np.median(data[start:end])
            
        return background
    
    def remove_background(self, data: np.ndarray, background: np.ndarray) -> np.ndarray:
        """Remove background signal."""
        return data - background
