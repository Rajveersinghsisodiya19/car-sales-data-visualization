import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("car_sales_data.csv")

# MATPLOTLIB PLOTS


#  Line Plot 
avg_price_per_year = df.groupby('Year of manufacture')['Price'].mean()
plt.figure(figsize=(7,5))
plt.plot(avg_price_per_year.index, avg_price_per_year.values, marker='o')
plt.xlabel('Year of manufacture')
plt.ylabel('Average Price')
plt.title('Average Car Price by Year of Manufacture')
plt.grid(True)
plt.show()

#  Bar Chart 
avg_price_per_brand = df.groupby('Manufacturer')['Price'].mean()
plt.figure(figsize=(10,5))
plt.bar(avg_price_per_brand.index, avg_price_per_brand.values, color='orange')
plt.xlabel('Manufacturer')
plt.ylabel('Average Price')
plt.title('Average Price by Manufacturer')
plt.xticks(rotation=45)
plt.show()

#  Scatter Plot 
plt.figure(figsize=(7,5))
plt.scatter(df['Engine size'], df['Price'], alpha=0.7)
plt.xlabel('Engine size')
plt.ylabel('Price')
plt.title('Engine Size vs Price')
plt.show()

# Histogram 
plt.figure(figsize=(7,5))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Car Prices')
plt.show()

#  Box Plot – Price by Fuel type
plt.figure(figsize=(7,5))
df.boxplot(column='Price', by='Fuel type', grid=False)
plt.title('Price Distribution by Fuel Type')
plt.suptitle('')
plt.xlabel('Fuel type')
plt.ylabel('Price')
plt.show()



# SEABORN PLOTS



#  Heatmap 
plt.figure(figsize=(8,6))
sns.heatmap(df[['Engine size','Year of manufacture','Mileage','Price']].corr(),
            annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

#  Violinplot
plt.figure(figsize=(10,6))
sns.violinplot(x='Manufacturer', y='Price', data=df, inner='box')
plt.title('Price Distribution by Manufacturer')
plt.xticks(rotation=45)
plt.show()

#  Pairplot 
sns.pairplot(df[['Engine size','Year of manufacture','Mileage','Price']])
plt.suptitle('Pairwise Feature Relationships', y=1.02)
plt.show()

#  Countplot 
plt.figure(figsize=(6,4))
sns.countplot(x='Fuel type', data=df)
plt.title('Count of Cars by Fuel Type')
plt.show()

# Regplot 
plt.figure(figsize=(7,5))
sns.regplot(x='Mileage', y='Price', data=df, scatter_kws={'alpha':0.6})
plt.title('Mileage vs Price with Trendline')
plt.show()
