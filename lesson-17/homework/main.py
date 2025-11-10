import pandas as pd
import numpy as np

print("="*50)
print("HOMEWORK 1")
print("="*50)

# Create the initial DataFrame
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename column names using function
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print("\n1. DataFrame with renamed columns:")
print(df)

# 2. Print the first 3 rows of the DataFrame
print("\n2. First 3 rows:")
print(df.head(3))

# 3. Find the mean age of the individuals
mean_age = df['age'].mean()
print(f"\n3. Mean age: {mean_age}")

# 4. Select and print only the 'Name' and 'City' columns
print("\n4. 'first_name' and 'City' columns:")
print(df[['first_name', 'City']])

# 5. Add a new column 'Salary' with random salary values
np.random.seed(42)  # For reproducibility
df['Salary'] = np.random.randint(40000, 100000, size=len(df))
print("\n5. DataFrame with 'Salary' column:")
print(df)

# 6. Display summary statistics of the DataFrame
print("\n6. Summary statistics:")
print(df.describe())

print("\n" + "="*50)
print("HOMEWORK 2")
print("="*50)

# 1. Create a DataFrame named sales_and_expenses
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})
print("\n1. sales_and_expenses DataFrame:")
print(sales_and_expenses)

# 2. Calculate and display the maximum sales and expenses
print("\n2. Maximum sales and expenses:")
print(f"Maximum Sales: {sales_and_expenses['Sales'].max()}")
print(f"Maximum Expenses: {sales_and_expenses['Expenses'].max()}")

# 3. Calculate and display the minimum sales and expenses
print("\n3. Minimum sales and expenses:")
print(f"Minimum Sales: {sales_and_expenses['Sales'].min()}")
print(f"Minimum Expenses: {sales_and_expenses['Expenses'].min()}")

# 4. Calculate and display the average sales and expenses
print("\n4. Average sales and expenses:")
print(f"Average Sales: {sales_and_expenses['Sales'].mean()}")
print(f"Average Expenses: {sales_and_expenses['Expenses'].mean()}")

print("\n" + "="*50)
print("HOMEWORK 3")
print("="*50)

# 1. Create a DataFrame named expenses
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})
print("\n1. expenses DataFrame:")
print(expenses)

# Set Category as index
expenses = expenses.set_index('Category')
print("\nDataFrame with Category as index:")
print(expenses)

# 2. Calculate and display the maximum expense for each category
print("\n2. Maximum expense for each category:")
print(expenses.max(axis=1))

# 3. Calculate and display the minimum expense for each category
print("\n3. Minimum expense for each category:")
print(expenses.min(axis=1))

# 4. Calculate and display the average expense for each category
print("\n4. Average expense for each category:")
print(expenses.mean(axis=1))
