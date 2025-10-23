"""
Configuration settings for Panopto Video Analytics Project
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent

# Data file paths
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"
EXPORTS_PATH = PROJECT_ROOT / "data" / "exports"

# Visualization settings
PLOT_STYLE = 'seaborn-v0_8'
COLOR_PALETTE = 'husl'
FIGURE_SIZE = (12, 8)
DPI = 300

# Dashboard settings
DASHBOARD_TITLE = "Panopto Video Analytics Dashboard"
REFRESH_INTERVAL = 30  # minutes

# File naming conventions
EXCEL_FILE_PATTERN = "*.xlsx"
PROCESSED_DATA_FILENAME = "combined_panopto_data.csv"
SUMMARY_REPORT_FILENAME = "panopto_summary_report.html"