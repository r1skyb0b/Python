import pandas as pd
import numpy as np
import sqlite3

# ==========================================
# HOMEWORK ASSIGNMENT 1: Analyzing Sales Data
# ==========================================

print("=" * 60)
print("HOMEWORK ASSIGNMENT 1: Analyzing Sales Data")
print("=" * 60)

# Read the sales data
sales_df = pd.read_csv('sales_data.csv')

# Convert Date column to datetime
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

print("\nDataset Preview:")
print(sales_df.head())
print(f"\nTotal records: {len(sales_df)}")

# Task 1: Group by Category and calculate aggregate statistics
print("\n" + "-" * 60)
print("TASK 1: Aggregate Statistics by Category")
print("-" * 60)

category_stats = sales_df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],
    'Price': 'mean'
}).round(2)

# Flatten column names
category_stats.columns = ['Total_Quantity_Sold', 'Max_Quantity_Single_Transaction', 'Avg_Price_Per_Unit']
category_stats = category_stats.reset_index()

print("\nCategory Statistics:")
print(category_stats.to_string(index=False))

# Task 2: Top-selling product in each category
print("\n" + "-" * 60)
print("TASK 2: Top-Selling Product in Each Category")
print("-" * 60)

# Calculate total quantity sold per product
product_totals = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
product_totals.columns = ['Category', 'Product', 'Total_Quantity']

# Get the top product in each category
top_products = product_totals.loc[product_totals.groupby('Category')['Total_Quantity'].idxmax()]

print("\nTop-Selling Products:")
print(top_products.to_string(index=False))

# Task 3: Find date with highest total sales
print("\n" + "-" * 60)
print("TASK 3: Date with Highest Total Sales")
print("-" * 60)

# Calculate total sales for each transaction
sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']

# Group by date and sum total sales
daily_sales = sales_df.groupby('Date')['Total_Sales'].sum().reset_index()
daily_sales.columns = ['Date', 'Total_Sales']

# Find the date with maximum sales
max_sales_date = daily_sales.loc[daily_sales['Total_Sales'].idxmax()]

print(f"\nDate with Highest Total Sales:")
print(f"Date: {max_sales_date['Date'].strftime('%Y-%m-%d')}")
print(f"Total Sales: ${max_sales_date['Total_Sales']:,.2f}")

# ==========================================
# HOMEWORK ASSIGNMENT 2: Examining Customer Orders
# ==========================================

print("\n\n" + "=" * 60)
print("HOMEWORK ASSIGNMENT 2: Examining Customer Orders")
print("=" * 60)

# Read the customer orders data
orders_df = pd.read_csv('customer_orders.csv')

print("\nDataset Preview:")
print(orders_df.head())
print(f"\nTotal records: {len(orders_df)}")

# Task 1: Filter customers with at least 20 orders
print("\n" + "-" * 60)
print("TASK 1: Customers with 20+ Orders")
print("-" * 60)

# Count orders per customer
customer_order_counts = orders_df.groupby('CustomerID').size().reset_index(name='Order_Count')

# Filter customers with at least 20 orders
customers_20plus = customer_order_counts[customer_order_counts['Order_Count'] >= 20]

print(f"\nCustomers with 20 or more orders:")
print(customers_20plus.to_string(index=False))

if len(customers_20plus) == 0:
    print("\nNote: No customers have made 20 or more orders in this dataset.")

# Task 2: Customers with average price > $120
print("\n" + "-" * 60)
print("TASK 2: Customers with Average Price > $120")
print("-" * 60)

# Calculate average price per customer
customer_avg_price = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
customer_avg_price.columns = ['CustomerID', 'Avg_Price_Per_Unit']
customer_avg_price['Avg_Price_Per_Unit'] = customer_avg_price['Avg_Price_Per_Unit'].round(2)

# Filter customers with average price > $120
customers_high_avg = customer_avg_price[customer_avg_price['Avg_Price_Per_Unit'] > 120]

print(f"\nCustomers with average price per unit > $120:")
print(customers_high_avg.to_string(index=False))

if len(customers_high_avg) == 0:
    print("\nNote: No customers have an average price per unit greater than $120.")

# Task 3: Products with total quantity >= 5
print("\n" + "-" * 60)
print("TASK 3: Products with Total Quantity >= 5")
print("-" * 60)

# Calculate total quantity and total price for each product
product_summary = orders_df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': lambda x: (orders_df.loc[x.index, 'Quantity'] * orders_df.loc[x.index, 'Price']).sum()
}).reset_index()

product_summary.columns = ['Product', 'Total_Quantity', 'Total_Price']

# Filter products with total quantity >= 5
products_filtered = product_summary[product_summary['Total_Quantity'] >= 5]
products_filtered = products_filtered.sort_values('Total_Quantity', ascending=False)

print(f"\nProducts with total quantity >= 5 units:")
print(f"(Showing {len(products_filtered)} out of {len(product_summary)} total products)")
print(products_filtered.to_string(index=False))

# ==========================================
# HOMEWORK ASSIGNMENT 3: Population Salary Analysis
# ==========================================

print("\n\n" + "=" * 60)
print("HOMEWORK ASSIGNMENT 3: Population Salary Analysis")
print("=" * 60)

# Step 1: Read salary bands from Excel file
print("\nReading salary band definitions from Excel...")
try:
    # Adjust the sheet name if needed
    salary_bands_df = pd.read_excel('population salary analysis.xlsx', sheet_name=0)
    print("\nSalary Bands:")
    print(salary_bands_df)
    
    # Expected columns: 'Salary_Band', 'Min_Salary', 'Max_Salary' or similar
    # Adjust column names based on your actual Excel file structure
    
except FileNotFoundError:
    print("\nWARNING: 'population salary analysis.xlsx' not found!")
    print("Creating sample salary bands for demonstration...")
    # Sample salary bands (adjust these based on your actual data)
    salary_bands_df = pd.DataFrame({
        'Salary_Band': ['Low', 'Medium', 'High', 'Very High'],
        'Min_Salary': [0, 30000, 60000, 100000],
        'Max_Salary': [29999, 59999, 99999, float('inf')]
    })
    print(salary_bands_df)

# Step 2: Read population data from SQLite database using SQL
print("\n\nReading population data from database...")
try:
    conn = sqlite3.connect('population.db')
    
    # Use SQL ONLY to SELECT data from database (as per requirement)
    # All calculations will be done in Python/pandas
    query = "SELECT * FROM population"
    population_df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    print(f"\nPopulation Data Preview:")
    print(population_df.head())
    print(f"\nTotal records: {len(population_df)}")
    print(f"\nColumns: {list(population_df.columns)}")
    
    # Expected columns might include: 'ID', 'State', 'Salary', etc.
    # Adjust based on your actual database schema
    
except (sqlite3.OperationalError, FileNotFoundError) as e:
    print(f"\nWARNING: Could not read from database - {e}")
    print("Creating sample population data for demonstration...")
    # Sample data (adjust based on your actual schema)
    np.random.seed(42)
    population_df = pd.DataFrame({
        'ID': range(1, 101),
        'State': np.random.choice(['CA', 'NY', 'TX', 'FL'], 100),
        'Salary': np.random.randint(20000, 150000, 100)
    })
    print(population_df.head())

# Step 3: Assign salary bands to each person
print("\n\nAssigning salary bands...")

def assign_salary_band(salary, bands_df):
    """Assign salary band based on salary value"""
    for idx, row in bands_df.iterrows():
        if row['Min_Salary'] <= salary <= row['Max_Salary']:
            return row['Salary_Band']
    return 'Unknown'

population_df['Salary_Band'] = population_df['Salary'].apply(
    lambda x: assign_salary_band(x, salary_bands_df)
)

# Step 4: Calculate overall statistics by salary category
print("\n" + "-" * 60)
print("OVERALL ANALYSIS: Statistics by Salary Category")
print("-" * 60)

total_population = len(population_df)

overall_stats = population_df.groupby('Salary_Band').agg({
    'Salary': ['count', 'mean', 'median']
}).round(2)

overall_stats.columns = ['Population_Count', 'Average_Salary', 'Median_Salary']
overall_stats = overall_stats.reset_index()

# Calculate percentage
overall_stats['Percentage_of_Population'] = (
    (overall_stats['Population_Count'] / total_population) * 100
).round(2)

# Reorder columns
overall_stats = overall_stats[['Salary_Band', 'Population_Count', 
                               'Percentage_of_Population', 'Average_Salary', 
                               'Median_Salary']]

print("\nOverall Salary Category Statistics:")
print(overall_stats.to_string(index=False))

# Step 5: Calculate statistics by State and Salary Category
print("\n" + "-" * 60)
print("STATE-LEVEL ANALYSIS: Statistics by State and Salary Category")
print("-" * 60)

# Get unique states
states = population_df['State'].unique()

for state in sorted(states):
    print(f"\n{'=' * 40}")
    print(f"State: {state}")
    print('=' * 40)
    
    state_data = population_df[population_df['State'] == state]
    state_total = len(state_data)
    
    state_stats = state_data.groupby('Salary_Band').agg({
        'Salary': ['count', 'mean', 'median']
    }).round(2)
    
    state_stats.columns = ['Population_Count', 'Average_Salary', 'Median_Salary']
    state_stats = state_stats.reset_index()
    
    # Calculate percentage for this state
    state_stats['Percentage_of_Population'] = (
        (state_stats['Population_Count'] / state_total) * 100
    ).round(2)
    
    # Reorder columns
    state_stats = state_stats[['Salary_Band', 'Population_Count', 
                               'Percentage_of_Population', 'Average_Salary', 
                               'Median_Salary']]
    
    print(f"\nTotal population in {state}: {state_total}")
    print(state_stats.to_string(index=False))

# Step 6: Summary comparison across states
print("\n" + "-" * 60)
print("SUMMARY: Average Salary by State")
print("-" * 60)

state_summary = population_df.groupby('State').agg({
    'Salary': ['count', 'mean', 'median']
}).round(2)

state_summary.columns = ['Total_Population', 'Average_Salary', 'Median_Salary']
state_summary = state_summary.reset_index()
state_summary = state_summary.sort_values('Average_Salary', ascending=False)

print("\nState Salary Summary:")
print(state_summary.to_string(index=False))

print("\n" + "=" * 60)
print("ALL ASSIGNMENTS COMPLETE")
print("=" * 60)
