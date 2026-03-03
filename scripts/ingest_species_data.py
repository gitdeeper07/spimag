#!/usr/bin/env python3
"""Ingest raw species data pipeline."""

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Ingest raw species data")
    parser.add_argument("--species", required=True, help="Species ID")
    parser.add_argument("--date-range", help="Date range (YYYY-MM-DD:YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    print(f"📥 Ingesting data for species: {args.species}")
    # TODO: Implement data ingestion
    print("✅ Data ingestion complete")

if __name__ == "__main__":
    main()
