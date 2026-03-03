"""Dashboard data export utilities."""

import json
import csv
from typing import Dict, List, Optional
from datetime import datetime
import numpy as np


class DashboardExporter:
    """Export data for web dashboard."""
    
    def __init__(self, output_dir: str = "dashboard/public/data/"):
        self.output_dir = output_dir
        
    def export_smni_timeseries(self, data: List[Dict], filename: str = "smni_timeseries.json"):
        """Export SMNI time series data."""
        output = []
        for item in data:
            output.append({
                'timestamp': item.get('timestamp', datetime.now().isoformat()),
                'species': item.get('species', 'unknown'),
                'smni': float(item.get('smni', 0)),
                'alert_level': item.get('alert_level', 'BACKGROUND')
            })
        
        with open(f"{self.output_dir}{filename}", 'w') as f:
            json.dump(output, f, indent=2)
    
    def export_species_summary(self, species_data: Dict, filename: str = "species_summary.json"):
        """Export species summary data."""
        with open(f"{self.output_dir}{filename}", 'w') as f:
            json.dump(species_data, f, indent=2)
    
    def export_storm_status(self, storm_data: Dict, filename: str = "storm_status.json"):
        """Export geomagnetic storm status."""
        with open(f"{self.output_dir}{filename}", 'w') as f:
            json.dump(storm_data, f, indent=2)
    
    def export_parameters_csv(self, parameters: List[Dict], filename: str = "parameters.csv"):
        """Export parameters as CSV."""
        if not parameters:
            return
            
        fieldnames = parameters[0].keys()
        
        with open(f"{self.output_dir}{filename}", 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(parameters)
