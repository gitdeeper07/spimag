"""Geomagnetic storm impact modeling."""

import numpy as np
from typing import Optional, Dict, Tuple
from datetime import datetime, timedelta


class GeomagneticStormImpact:
    """Model geomagnetic storm effects on SMNI."""
    
    def __init__(self):
        pass
    
    def compute_smni_reduction(self, kp_index: int, latitude: float) -> float:
        """Compute SMNI reduction factor due to storm."""
        # Base reduction from Kp index (0-9)
        base_reduction = min(kp_index / 9.0, 1.0) * 0.5
        
        # Latitude factor (stronger at high latitudes)
        lat_factor = abs(latitude) / 90.0
        
        reduction = base_reduction * (0.5 + 0.5 * lat_factor)
        return min(reduction, 0.7)  # Max 70% reduction
    
    def storm_alert_level(self, kp_index: int) -> str:
        """Get alert level based on Kp index."""
        if kp_index >= 8:
            return "CRITICAL"
        elif kp_index >= 6:
            return "EMERGENCY"
        elif kp_index >= 4:
            return "ALERT"
        elif kp_index >= 3:
            return "WATCH"
        else:
            return "BACKGROUND"
    
    def affected_region(self, kp_index: int) -> str:
        """Get affected geographic region."""
        if kp_index >= 7:
            return "45-65°N"
        elif kp_index >= 5:
            return "55-65°N"
        else:
            return ">60°N"
