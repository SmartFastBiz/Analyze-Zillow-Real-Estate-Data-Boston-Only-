import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

os.makedirs('/home/claude/images', exist_ok=True)

df = pd.read_csv('/home/claude/zillow_listings.csv')

sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams.update({'figure.dpi': 130, 'font.family': 'DejaVu Sans'})
BLUE = '#2563EB'
GREEN = '#16A34A'
RED = '#EF4444'

# 1. Missing values
fig, ax = plt.subplots(figsize=(10, 3.5))
missing = df.isnull().sum().reset_index()
missing.columns = ['column', 'missing']
missing['pct'] = (missing['missing'] / len(df) * 100).round(2)
missing_only = missing[missing['missing'] > 0]
bars = ax.barh(missing_only['column'], missing_only['pct'], color=RED)
ax.set_xlabel('Missing (%)')
ax.set_title('Missing Values by Column', fontweight='bold', pad=10)
for bar, v in zip(bars, missing_only['pct']):
    ax.text(v + 0.1, bar.get_y() + bar.get_height()/2, f'{v}%', va='center', fontsize=10)
plt.tight_layout()
plt.savefig('/home/claude/images/01_missing_values.png')
plt.close()
print("Plot 1 done")

# 2. Median price by neighborhood
fig, ax = plt.subplots(figsize=(13, 5.5))
order = df.groupby('neighborhood')['list_price'].median().sort_values(ascending=False).index
medians = df.groupby('neighborhood')['list_price'].median().reindex(order)
colors = [BLUE if m >= 750000 else GREEN for m in medians]
bars = ax.bar(range(len(order)), medians.values / 1000, color=colors, edgecolor='white', linewidth=0.8)
ax.set_ylabel('Median List Price ($K)')
ax.set_title('Median Home Price by Boston Neighborhood', fontweight='bold', pad=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}K'))
ax.set_xticks(range(len(order)))
ax.set_xticklabels(list(order), rotation=35, ha='right')
for bar, v in zip(bars, medians.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 4,
            f'${v/1000:.0f}K', ha='center', va='bottom', fontsize=7.5, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/images/02_price_by_neighborhood.png')
plt.close()
print("Plot 2 done")

# 3. Price per sqft violin - top 8 neighborhoods
top8 = df['neighborhood'].value_counts().head(8).index.tolist()
df_top8 = df[df['neighborhood'].isin(top8)]
order3 = df_top8.groupby('neighborhood')['price_per_sqft'].median().sort_values(ascending=False).index.tolist()
fig, ax = plt.subplots(figsize=(13, 5.5))
sns.violinplot(data=df_top8, x='neighborhood', y='price_per_sqft', order=order3,
               hue='neighborhood', palette='Blues_d', inner='quartile', legend=False, ax=ax)
ax.set_xticks(range(len(order3)))
ax.set_xticklabels(order3, rotation=30, ha='right')
ax.set_ylabel('Price per Sq Ft ($)')
ax.set_title('Price per Sq Ft Distribution — Top 8 Neighborhoods', fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig('/home/claude/images/03_ppsf_violin.png')
plt.close()
print("Plot 3 done")

# 4. Price vs sqft scatter
fig, ax = plt.subplots(figsize=(9, 5.5))
sample = df.sample(600, random_state=1)
scatter = ax.scatter(sample['sqft'], sample['list_price']/1000,
                     c=sample['bedrooms'], cmap='YlOrRd', alpha=0.6, s=28, edgecolors='none')
cb = plt.colorbar(scatter, ax=ax)
cb.set_label('Bedrooms')
m, b = np.polyfit(df['sqft'], df['list_price']/1000, 1)
x_line = np.linspace(df['sqft'].min(), df['sqft'].max(), 200)
ax.plot(x_line, m*x_line + b, color='black', linewidth=1.5, linestyle='--', label='Trend line')
ax.legend()
ax.set_xlabel('Square Footage')
ax.set_ylabel('List Price ($K)')
ax.set_title('Price vs. Square Footage — Boston, MA (colored by Bedrooms)', fontweight='bold', pad=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}K'))
plt.tight_layout()
plt.savefig('/home/claude/images/04_price_vs_sqft.png')
plt.close()
print("Plot 4 done")

# 5. Avg price by property type
fig, ax = plt.subplots(figsize=(8, 4.5))
pt_order = df.groupby('property_type')['list_price'].mean().sort_values(ascending=False).index.tolist()
means = df.groupby('property_type')['list_price'].mean().reindex(pt_order)
pal = sns.color_palette('Set2', len(pt_order))
bars = ax.bar(pt_order, means.values/1000, color=pal, edgecolor='white')
ax.set_ylabel('Avg List Price ($K)')
ax.set_title('Average Price by Property Type — Boston, MA', fontweight='bold', pad=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}K'))
for bar, v in zip(bars, means.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 4,
            f'${v/1000:.0f}K', ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/images/05_price_by_type.png')
plt.close()
print("Plot 5 done")

# 6. Days on market by neighborhood (top 10)
top10 = df['neighborhood'].value_counts().head(10).index.tolist()
df_top10 = df[df['neighborhood'].isin(top10)]
dom_order = df_top10.groupby('neighborhood')['days_on_market'].median().sort_values().index.tolist()
fig, ax = plt.subplots(figsize=(13, 5))
sns.boxplot(data=df_top10, x='neighborhood', y='days_on_market', order=dom_order,
            hue='neighborhood', palette='Greens_d', legend=False,
            flierprops=dict(markersize=2, alpha=0.4), ax=ax)
ax.set_xticks(range(len(dom_order)))
ax.set_xticklabels(dom_order, rotation=30, ha='right')
ax.set_ylabel('Days on Market')
ax.set_title('Days on Market by Neighborhood — Boston, MA', fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig('/home/claude/images/06_dom_by_neighborhood.png')
plt.close()
print("Plot 6 done")

# 7. Correlation heatmap
fig, ax = plt.subplots(figsize=(9, 7))
num_cols = ['list_price','sqft','bedrooms','bathrooms','year_built','days_on_market','price_per_sqft','hoa_monthly_fee']
corr = df[num_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5, ax=ax, annot_kws={'size': 9})
ax.set_title('Correlation Matrix of Numeric Features — Boston, MA', fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig('/home/claude/images/07_correlation.png')
plt.close()
print("Plot 7 done")

# 8. YoY price trend by neighborhood (top 5)
fig, ax = plt.subplots(figsize=(10, 5))
yearly = df.groupby(['list_year','neighborhood'])['list_price'].median().reset_index()
top5 = df['neighborhood'].value_counts().head(5).index.tolist()
pal2 = sns.color_palette('tab10', len(top5))
for nbhd, color in zip(top5, pal2):
    sub = yearly[yearly['neighborhood'] == nbhd]
    ax.plot(sub['list_year'], sub['list_price']/1000, marker='o', label=nbhd, color=color, linewidth=2)
ax.set_xlabel('Year')
ax.set_ylabel('Median List Price ($K)')
ax.set_title('Median Price Trend (2021–2024) — Top 5 Boston Neighborhoods', fontweight='bold', pad=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}K'))
ax.legend(loc='upper left', fontsize=8)
ax.set_xticks([2021,2022,2023,2024])
plt.tight_layout()
plt.savefig('/home/claude/images/08_price_trend.png')
plt.close()
print("Plot 8 done")

# 9. Zestimate accuracy
fig, ax = plt.subplots(figsize=(7, 5.5))
diff_pct = ((df['zestimate'] - df['list_price']) / df['list_price'] * 100)
ax.hist(diff_pct, bins=50, color=BLUE, edgecolor='white', alpha=0.85)
ax.axvline(0, color='red', linewidth=1.5, linestyle='--', label='Perfect estimate')
ax.axvline(diff_pct.mean(), color='orange', linewidth=1.5, linestyle='--', label=f'Mean: {diff_pct.mean():.1f}%')
ax.set_xlabel('Zestimate vs List Price (%)')
ax.set_ylabel('Number of Listings')
ax.set_title("Zillow Zestimate Accuracy vs List Price — Boston, MA", fontweight='bold', pad=10)
ax.legend()
plt.tight_layout()
plt.savefig('/home/claude/images/09_zestimate_accuracy.png')
plt.close()
print("Plot 9 done")

print("\nAll plots saved!")
