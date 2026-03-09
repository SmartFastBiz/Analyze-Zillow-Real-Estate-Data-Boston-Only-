# 🏠 Boston, MA Real Estate Market Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-lightblue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green)

Exploratory data analysis of ~1,500 residential property listings across **15 Boston neighborhoods** (2021–2024). This project covers data cleaning, feature engineering, and visualization to uncover what drives home prices in the Greater Boston market.

---

## 📋 Table of Contents
- [Project Goals](#project-goals)
- [Dataset](#dataset)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Next Steps](#next-steps)

---

## 🎯 Project Goals

1. Identify which Boston neighborhoods have the highest prices and fastest-moving markets
2. Understand which home features most strongly correlate with price
3. Track year-over-year price appreciation across neighborhoods
4. Evaluate Zillow Zestimate accuracy vs. actual list prices

---

## 📊 Dataset

The dataset contains **1,500 listings** across 15 Boston neighborhoods with the following features:

| Column | Type | Description |
|--------|------|-------------|
| `listing_id` | string | Unique property identifier |
| `city` | string | City (Boston, MA) |
| `neighborhood` | string | Boston neighborhood |
| `property_type` | string | Single Family / Condo / Townhouse / Multi-Family |
| `bedrooms` | int | Number of bedrooms |
| `bathrooms` | float | Number of bathrooms |
| `sqft` | int | Interior square footage |
| `year_built` | int | Year of construction |
| `garage_spaces` | int | Number of garage spaces |
| `has_pool` | int | Pool (1 = yes, 0 = no) |
| `hoa_monthly_fee` | float | HOA dues in USD (NaN = no HOA) |
| `list_price` | int | Asking price in USD |
| `zestimate` | int | Zillow automated valuation |
| `price_per_sqft` | float | List price ÷ sqft |
| `days_on_market` | int | Days active before sold/removed |
| `list_year` | int | Year listed (2021–2024) |

**Neighborhoods covered:** Back Bay · Beacon Hill · South Boston · South End · Charlestown · Jamaica Plain · Fenway · Dorchester · East Boston · Allston/Brighton · West Roxbury · Roslindale · Roxbury · Hyde Park · Mattapan

---

## 🔍 Key Findings

| # | Finding |
|---|---------|
| 1 | **Back Bay & Beacon Hill are the priciest neighborhoods** — highest median price and $/sqft in Boston |
| 2 | **Square footage is the #1 price driver** — strongest positive correlation with list price |
| 3 | **Multi-family homes average the highest prices** due to rental income potential |
| 4 | **South Boston & Charlestown saw strong year-over-year appreciation** from 2021–2024 |
| 5 | **Zestimate accuracy is strong** — over 70% of listings priced within ±5% of Zestimate |
| 6 | **Days-on-market varies by neighborhood** — high-demand areas like South End move significantly faster |

---

## 📈 Visualizations

The notebook produces 9 publication-quality charts:

- **Missing values audit** — identifying and quantifying data gaps
- **Median price by neighborhood** — bar chart ranked by market cost
- **Price-per-sqft violin plot** — distribution comparison across top 8 neighborhoods
- **Price vs. square footage scatter** — with trend line, colored by bedroom count
- **Average price by property type** — bar chart with labels
- **Days on market boxplot** — market speed comparison by neighborhood
- **Correlation heatmap** — numeric feature relationships
- **Year-over-year price trend** — line chart for top 5 neighborhoods (2021–2024)
- **Zestimate accuracy histogram** — how close automated valuations are to list prices

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Run the Notebook
```bash
git clone https://github.com/YOUR_USERNAME/boston-real-estate-eda.git
cd boston-real-estate-eda
jupyter notebook zillow_eda.ipynb
```

Or regenerate the data and charts directly:
```bash
python generate_data.py    # Creates zillow_listings.csv
python generate_plots.py   # Creates images/ folder with all charts
```

---

## 📁 Project Structure

```
boston-real-estate-eda/
│
├── zillow_eda.ipynb               # Main analysis notebook
├── zillow_listings.csv            # Dataset (1,500 Boston listings)
├── generate_data.py               # Script to regenerate the dataset
├── generate_plots.py              # Script to regenerate all charts
├── images/                        # Saved visualization outputs
│   ├── 01_missing_values.png
│   ├── 02_price_by_neighborhood.png
│   ├── 03_ppsf_violin.png
│   ├── 04_price_vs_sqft.png
│   ├── 05_price_by_type.png
│   ├── 06_dom_by_neighborhood.png
│   ├── 07_correlation.png
│   ├── 08_price_trend.png
│   └── 09_zestimate_accuracy.png
└── README.md
```

---

## 🔮 Next Steps

- [ ] Build a **price prediction model** (Linear Regression, Random Forest)
- [ ] Add **interactive neighborhood maps** with Folium
- [ ] Analyze **seasonal listing trends** with monthly data
- [ ] Expand dataset to **Greater Boston suburbs** (Cambridge, Somerville, Brookline)

---

## 🛠️ Tools Used

- **Python 3.11** — core language
- **Pandas** — data manipulation and cleaning
- **NumPy** — numerical operations
- **Matplotlib** — base charting library
- **Seaborn** — statistical visualizations
- **Jupyter Notebook** — interactive analysis environment

---

*Dataset is simulated Zillow-style data for educational purposes.*
