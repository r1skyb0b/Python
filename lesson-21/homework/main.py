import pandas as pd
import matplotlib.pyplot as plt

# ========== DataFrame 1: Student Grades ==========
print("=" * 60)
print("DATAFRAME 1: STUDENT GRADES")
print("=" * 60)

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)
print("\nOriginal DataFrame:")
print(df1)

# Exercise 1: Calculate the average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print("\nExercise 1: Average grade for each student")
print(df1[['Student_ID', 'Average']])

# Exercise 2: Find the student with the highest average grade
highest_avg_student = df1.loc[df1['Average'].idxmax()]
print(f"\nExercise 2: Student with highest average grade")
print(f"Student ID: {highest_avg_student['Student_ID']}, Average: {highest_avg_student['Average']:.2f}")

# Exercise 3: Create a new column 'Total'
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print("\nExercise 3: Total marks for each student")
print(df1[['Student_ID', 'Total']])

# Exercise 4: Plot a bar chart for average grades in each subject
subject_averages = df1[['Math', 'English', 'Science']].mean()
plt.figure(figsize=(10, 6))
subject_averages.plot(kind='bar', color=['#3498db', '#e74c3c', '#2ecc71'])
plt.title('Average Grades by Subject', fontsize=14, fontweight='bold')
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Grade', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# ========== DataFrame 2: Sales Data ==========
print("\n" + "=" * 60)
print("DATAFRAME 2: SALES DATA")
print("=" * 60)

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)
print("\nOriginal DataFrame:")
print(df2)

# Exercise 1: Calculate total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("\nExercise 1: Total sales for each product")
print(total_sales)

# Exercise 2: Find the date with highest total sales
df2['Daily_Total'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Daily_Total'].idxmax(), 'Date']
highest_sales_amount = df2['Daily_Total'].max()
print(f"\nExercise 2: Date with highest total sales")
print(f"Date: {highest_sales_date.strftime('%Y-%m-%d')}, Total Sales: {highest_sales_amount}")

# Exercise 3: Calculate percentage change in sales
df2['Product_A_pct_change'] = df2['Product_A'].pct_change() * 100
df2['Product_B_pct_change'] = df2['Product_B'].pct_change() * 100
df2['Product_C_pct_change'] = df2['Product_C'].pct_change() * 100
print("\nExercise 3: Percentage change in sales")
print(df2[['Date', 'Product_A_pct_change', 'Product_B_pct_change', 'Product_C_pct_change']])

# Exercise 4: Plot line chart for sales trends
plt.figure(figsize=(12, 6))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A', linewidth=2)
plt.plot(df2['Date'], df2['Product_B'], marker='s', label='Product B', linewidth=2)
plt.plot(df2['Date'], df2['Product_C'], marker='^', label='Product C', linewidth=2)
plt.title('Sales Trends Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========== DataFrame 3: Employee Information ==========
print("\n" + "=" * 60)
print("DATAFRAME 3: EMPLOYEE INFORMATION")
print("=" * 60)

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)
print("\nOriginal DataFrame:")
print(df3)

# Exercise 1: Average salary for each department
avg_salary_dept = df3.groupby('Department')['Salary'].mean()
print("\nExercise 1: Average salary by department")
print(avg_salary_dept)

# Exercise 2: Employee with most experience
most_exp_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print(f"\nExercise 2: Employee with most experience")
print(f"Name: {most_exp_employee['Name']}, Experience: {most_exp_employee['Experience (Years)']} years")

# Exercise 3: Salary Increase percentage from minimum
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("\nExercise 3: Salary Increase percentage from minimum")
print(df3[['Name', 'Salary', 'Salary Increase']])

# Exercise 4: Bar chart for employee distribution
dept_counts = df3['Department'].value_counts()
plt.figure(figsize=(10, 6))
dept_counts.plot(kind='bar', color=['#9b59b6', '#1abc9c', '#f39c12'])
plt.title('Employee Distribution by Department', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# ========== DataFrame 4: Customer Orders ==========
print("\n" + "=" * 60)
print("DATAFRAME 4: CUSTOMER ORDERS")
print("=" * 60)

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)
print("\nOriginal DataFrame:")
print(df4)

# Exercise 1: Total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print(f"\nExercise 1: Total revenue from all orders: ${total_revenue}")

# Exercise 2: Most ordered product
most_ordered = df4['Product'].value_counts()
print(f"\nExercise 2: Most ordered product")
print(most_ordered)
print(f"Most ordered: Product {most_ordered.idxmax()} ({most_ordered.max()} orders)")

# Exercise 3: Average quantity of products ordered
avg_quantity = df4['Quantity'].mean()
print(f"\nExercise 3: Average quantity of products ordered: {avg_quantity:.2f}")

# Exercise 4: Pie chart for sales distribution
product_sales = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(8, 8))
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
plt.pie(product_sales, labels=[f'Product {p}' for p in product_sales.index], 
        autopct='%1.1f%%', startangle=90, colors=colors, explode=(0.05, 0.05, 0.05))
plt.title('Sales Distribution by Product', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("All exercises completed!")
print("=" * 60)
