# Unemployment Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("unemployment.csv")

# Data cleaning
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# View data
print(df.head())
print(df.describe())

# Unemployment trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Unemployment Rate'], color='blue')
plt.title("Unemployment Rate Trend")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.xticks(rotation=45)
plt.grid()
plt.show()


# COVID-19 impact
df['Period'] = df['Date'].apply(
    lambda x: 'COVID' if x >= pd.Timestamp('2020-03-01') else 'Before COVID'
)

covid = df.groupby('Period')['Unemployment Rate'].mean()

print("\nCOVID Impact:")
print(covid)


sns.barplot(x=covid.index, y=covid.values)
plt.title("COVID Impact on Unemployment")
plt.ylabel("Average Rate (%)")
plt.show()


# Seasonal trend
df['Month'] = df['Date'].dt.month

monthly = df.groupby('Month')['Unemployment Rate'].mean()

monthly.plot(marker='o', color='green')
plt.title("Seasonal Unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Average Rate (%)")
plt.grid()
plt.show()


# Insights
print("""
Insights:
- COVID-19 increased unemployment rates.
- Employment recovered after the pandemic.
- Seasonal patterns can be observed in monthly trends.
- Data can help governments create employment policies.
""")