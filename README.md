# Panopto Video Analytics Pipeline

## Project Overview
This pipeline is designed to provide insights and help educational institutions make data-driven decisions about their video learning resources.

## Research Questions

1. **Content Distribution Analysis**: Understanding the total minutes delivered across different media types
2. **Engagement Patterns**: Analyzing average duration and completion rates across course formats
3. **Usage Analytics**: Identifying viewing patterns and student engagement behaviors

## Technical Stack

- **Data Processing**: Python (pandas, numpy)
- **Visualization**: Plotly, Seaborn, Matplotlib
- **Development Environment**: Jupyter Notebooks, VS Code
- **Version Control**: Git/GitHub
- **Dashboard**: Tableau (optional)

## 📁 Project Structure

```
panopto-video-analytics/
├── README.md
├── requirements.txt
├── config.py
├── data/
│   ├── raw/              # Original data files (not tracked)
├── notebooks/
│   ├── notebook.ipynb    # Data exploration and cleaning (one course)
│   ├── course_analytics.ipynb 
├── scripts/
├── dashboards/
└── docs/                 # Documentation and guides
```

## Quick Start

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/panopto-video-analytics.git
cd panopto-video-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate         # On Mac 
source venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### How to use:
1. Store your data files in `data/raw/`
2. Run the notebooks of your interest either in google colab or on your local computer 

## Educational Impact

This pipeline helps educational institutions to optimize content creation based on student engagement data, improve student learning outcomes through data-backed insights, help make informed decisions about video production resources and track content effectiveness over time.

## Acknowledgments
This project is a semester-long course project in collaboration with Sheridan Center for Teaching and Learning and supported by Brown University Data Science Institue. For questions or collaboration opportunities, please open an issue or contact the maintainer.
