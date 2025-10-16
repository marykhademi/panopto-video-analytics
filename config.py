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

# Output paths
REPORTS_PATH = PROJECT_ROOT / "outputs" / "reports"
VISUALIZATIONS_PATH = PROJECT_ROOT / "outputs" / "visualizations"
DATA_QUALITY_PATH = PROJECT_ROOT / "outputs" / "data_quality"

# Analysis parameters
ENGAGEMENT_THRESHOLD = 1.0  # 100% completion rate threshold
MIN_VIEWS_THRESHOLD = 5     # Minimum views to consider for analysis
TOP_N_VIDEOS = 10          # Number of top videos to show in reports

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