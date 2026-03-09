import pandas as pd
import numpy as np

np.random.seed(42)
n = 1500

boston_cfg = {'base': 750000, 'sqft_base': 1400, 'growth': 0.07}

# Boston neighborhoods with price multipliers
neighborhoods = {
    'Back Bay':         1.45,
    'South End':        1.30,
    'Beacon Hill':      1.40,
    'Fenway':           1.05,
    'Charlestown':      1.20,
    'Jamaica Plain':    1.00,
    'Dorchester':       0.82,
    'Roxbury':          0.75,
    'East Boston':      0.90,
    'Allston/Brighton': 0.88,
    'Hyde Park':        0.80,
    'Roslindale':       0.85,
    'West Roxbury':     0.95,
    'South Boston':     1.25,
    'Mattapan':         0.72,
}
neighborhood_list = list(neighborhoods.keys())
neighborhood_probs = [0.08,0.09,0.06,0.07,0.07,0.08,0.09,0.06,0.07,0.07,0.05,0.05,0.05,0.08,0.03]

property_types = ['Single Family', 'Condo', 'Townhouse', 'Multi-Family']
type_multipliers = {'Single Family': 1.0, 'Condo': 0.75, 'Townhouse': 0.88, 'Multi-Family': 1.15}

rows = []

for i in range(n):
    city = 'Boston, MA'
    cfg = boston_cfg
    neighborhood = np.random.choice(neighborhood_list, p=neighborhood_probs)
    ptype = np.random.choice(property_types, p=[0.20, 0.45, 0.20, 0.15])
    mult = type_multipliers[ptype]
    nbhd_mult = neighborhoods[neighborhood]

    bedrooms = np.random.choice([1,2,3,4,5], p=[0.10, 0.30, 0.35, 0.18, 0.07])
    bathrooms = round(np.random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4], p=[0.08,0.10,0.30,0.18,0.20,0.09,0.05]), 1)
    sqft = int(np.random.normal(cfg['sqft_base'] * (0.7 + bedrooms * 0.15), 250))
    sqft = max(500, min(sqft, 5000))

    year_built = int(np.random.choice(range(1950, 2024), p=np.concatenate([
        np.linspace(0.002, 0.010, 37),
        np.linspace(0.010, 0.022, 37)
    ]) / np.sum(np.concatenate([np.linspace(0.002, 0.010, 37), np.linspace(0.010, 0.022, 37)]))))

    age = 2024 - year_built
    age_discount = max(0.70, 1.0 - age * 0.003)

    list_year = np.random.choice([2021, 2022, 2023, 2024], p=[0.15, 0.25, 0.35, 0.25])
    appreciation = (1 + cfg['growth']) ** (list_year - 2020)

    price = int(cfg['base'] * mult * nbhd_mult * (sqft / cfg['sqft_base']) * age_discount * appreciation * np.random.normal(1.0, 0.08))
    price = max(80000, price)

    days_on_market = int(np.random.exponential(22)) + 1
    days_on_market = min(days_on_market, 180)

    garage = np.random.choice([0, 1, 2, 3], p=[0.15, 0.25, 0.45, 0.15])
    pool = np.random.choice([0, 1], p=[0.72, 0.28])
    hoa_fee = int(np.random.choice([0, np.random.randint(50, 600)], p=[0.55, 0.45]))

    zestimate = int(price * np.random.normal(1.0, 0.04))
    price_per_sqft = round(price / sqft, 2)

    # inject a few realistic missing values
    if np.random.rand() < 0.04:
        hoa_fee = np.nan
    if np.random.rand() < 0.02:
        year_built = np.nan

    rows.append({
        'listing_id': f'ZL{100000+i}',
        'city': city,
        'neighborhood': neighborhood,
        'property_type': ptype,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft': sqft,
        'year_built': year_built,
        'garage_spaces': garage,
        'has_pool': pool,
        'hoa_monthly_fee': hoa_fee,
        'list_price': price,
        'zestimate': zestimate,
        'price_per_sqft': price_per_sqft,
        'days_on_market': days_on_market,
        'list_year': list_year,
    })

df = pd.DataFrame(rows)
df.to_csv('/home/claude/zillow_listings.csv', index=False)
print(f"Dataset created: {df.shape}")
print(df.dtypes)
print(df.head(3))
