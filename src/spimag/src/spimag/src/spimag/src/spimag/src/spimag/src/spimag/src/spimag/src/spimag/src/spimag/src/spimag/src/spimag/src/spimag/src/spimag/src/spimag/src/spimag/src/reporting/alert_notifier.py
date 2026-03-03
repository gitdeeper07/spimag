"""Alert notification generator."""

from typing import Dict, Optional, List
from datetime import datetime


class AlertNotifier:
    """Generate alert notifications for stakeholders."""
    
    def __init__(self):
        self.alert_levels = {
            'OPTIMAL': {'color': '🟢', 'action': 'Nominal monitoring'},
            'GOOD': {'color': '🟡', 'action': 'Standard tracking'},
            'MODERATE': {'color': '🟠', 'action': 'Enhanced monitoring'},
            'MARGINAL': {'color': '🔴', 'action': 'Alert stakeholders'},
            'DYSFUNCTIONAL': {'color': '⛔', 'action': 'Critical alert'}
        }
        
    def generate_alert(self, species: str, smni: float, 
                       alert_level: str, details: Dict) -> str:
        """Generate alert message."""
        level_info = self.alert_levels.get(alert_level, {})
        
        lines = []
        lines.append("=" * 60)
        lines.append(f"{level_info.get('color', '')} SPIMAG ALERT")
        lines.append("=" * 60)
        lines.append(f"\nTime: {datetime.now().isoformat()}")
        lines.append(f"Species: {species}")
        lines.append(f"SMNI Score: {smni:.3f}")
        lines.append(f"Alert Level: {alert_level}")
        lines.append(f"Action Required: {level_info.get('action', '')}")
        
        if details:
            lines.append("\nAdditional Details:")
            for key, value in details.items():
                lines.append(f"  • {key}: {value}")
        
        lines.append("\n" + "=" * 60)
        return "\n".join(lines)
