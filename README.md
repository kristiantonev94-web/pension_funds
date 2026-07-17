# 📈 Bulgarian Pension Funds Dashboard

A comprehensive Streamlit dashboard for analyzing Bulgarian UPF (Unit-Linked Fund) pension funds.

## 🚀 Features

- **Real-time Prices**: Track UPF pension fund prices in EUR
- **Membership Analytics**: Monitor insured persons and market share
- **Multi-page Interface**: Organized sections for different data views
- **Interactive Charts**: Plotly-powered visualizations
- **Data Export**: Download data as CSV
- **Responsive Design**: Works on desktop and mobile

## 📁 Project Structure

```
pension_funds/
├── app.py                    # Main entry point and landing page
├── config.py                 # Configuration and secrets management
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── pages/                    # Streamlit pages (auto-discovered)
│   ├── 1_📈_prices.py       # Prices dashboard
│   ├── 2_👥_members.py      # Insured persons dashboard
│   ├── 3_📊_analytics.py    # Analytics and insights
│   └── 4_⚙️_settings.py     # Settings and information
└── utils/                    # Reusable utility modules
    ├── __init__.py
    ├── data_loader.py       # Database queries and data fetching
    ├── data_processor.py    # Data transformation and calculations
    └── charts.py            # Reusable chart creation functions
```

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Databricks SQL Warehouse access
- Streamlit secrets configured

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd pension_funds
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure Streamlit secrets

Create `.streamlit/secrets.toml`:
```toml
[databricks]
server_hostname = "your-workspace.cloud.databricks.com"
http_path = "/sql/1.0/warehouses/your-warehouse-id"
access_token = "your-access-token"
```

### Running the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📊 Pages

### 1. 📈 Prices Dashboard
- Displays historical UPF pension fund prices
- Interactive line chart with fund comparison
- Data table with export functionality

### 2. 👥 Members Dashboard
- Shows insured persons trends
- Market share analysis with stacked area chart
- Current fund ranking
- Data table with export functionality

### 3. 📊 Analytics & Insights
- Advanced analysis (placeholder for future expansion)
- Performance metrics
- Comparative analysis

### 4. ⚙️ Settings
- Application information
- Technical details
- Support resources

## 🔄 Data Refresh

Data is cached for 1 hour to optimize performance. The cache TTL can be adjusted in `config.py`.

## 🎨 Customization

### Modifying Cache TTL
Edit `config.py`:
```python
CACHE_TTL = 3600  # Change to desired seconds
```

### Adding New Pages
1. Create a new file in the `pages/` directory with format: `N_emoji_name.py`
2. Streamlit will automatically discover and add it to the navigation
3. Use utilities from `utils/` for consistency

### Creating New Charts
Add functions to `utils/charts.py` for reusability across pages.

## 🤝 Contributing

To add new features:
1. Create a new branch: `git checkout -b feature/your-feature`
2. Make changes following the existing structure
3. Test thoroughly
4. Create a pull request

## 📝 License

This project is part of the Pension Funds Analytics initiative.

## 📞 Support

For issues or questions, contact the development team.
