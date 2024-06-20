import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'sales_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display summary statistics for the dataset
print("\nSummary statistics for the dataset:")
print(df.describe())

# Filter the data for a specific product
product_filter = df[df['Product'] == 'Product_A']
print("\nFiltered data for Product_A:")
print(product_filter.head())

# Sort the data by Sales in descending order
sorted_data = df.sort_values(by='Sales', ascending=False)
print("\nData sorted by Sales in descending order:")
print(sorted_data.head())

# Group the data by Region and calculate the mean Sales
grouped_data = df.groupby('Region')['Sales'].mean()
print("\nMean Sales by Region:")
print(grouped_data)

# Calculate summary statistics for Sales
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
std_sales = df['Sales'].std()

print("\nSummary statistics for Sales:")
print(f"Mean: {mean_sales}")
print(f"Median: {median_sales}")
print(f"Standard Deviation: {std_sales}")

# Visualize the distribution of Sales
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between Sales and Quantity
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='Sales', data=df)
plt.title('Sales vs. Quantity')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.show()

# Visualize Sales by Region using a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()
