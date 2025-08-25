import pandas as pd
import numpy as np

# ==================================================
# Step 1: Create Sample DataFrame
# ==================================================
print("=== Sample Data Creation ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Age': [25, 30, np.nan, 45, 29, 40, 30],
    'Salary': [50000, 60000, 52000, None, 58000, 62000, 50000],
    'Joining_Date': [
        '2020-01-15', '2019-05-20', '2021-07-01',
        '2018-03-12', '2020-08-30', '2017-09-17', '2019-11-11'
    ]
}
df = pd.DataFrame(data)
print(df)

# ==================================================
# Step 2: Data Cleaning
# ==================================================

# --- fillna() ---
# fillna() is used to replace missing values (NaN) with a given value.
# Use Case: If salary is missing, we can replace with average salary.
print("\n=== Fill Missing Salary with Mean (fillna) ===")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)

# --- dropna() ---
# dropna() is used to remove rows/columns with missing values.
# Use Case: If Age is missing and cannot be estimated, drop the row.
print("\n=== Drop Rows with Missing Age (dropna) ===")
df_clean = df.dropna(subset=['Age'])
print(df_clean)

# --- drop_duplicates() ---
# drop_duplicates() removes duplicate rows from DataFrame.
# Use Case: Prevent double-counting in datasets.
print("\n=== Remove Duplicate Rows (drop_duplicates) ===")
print(df_clean.drop_duplicates())

# ==================================================
# Step 3: Grouping & Aggregation
# ==================================================

# groupby() is used to split data into groups and apply aggregate functions.
# Use Case: Find average salary per department.
print("\n=== Average Salary per Department ===")
print(df_clean.groupby('Department')['Salary'].mean())

# Count employees per department
print("\n=== Count Employees per Department ===")
print(df_clean.groupby('Department')['Name'].count())

# ==================================================
# Step 4: Merging & Joining
# ==================================================

# merge() combines DataFrames using common columns (like SQL JOIN).
# Use Case: Merge employee info with marks.
df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame({'ID':[1,2,3], 'Marks':[85,90,78]})

print("\n=== Merge Example (SQL-like JOIN) ===")
merged = pd.merge(df1, df2, on='ID')
print(merged)

# concat() stacks DataFrames vertically or horizontally.
# Use Case: Combine datasets from multiple months.
print("\n=== Concat Example (Stack Vertically) ===")
concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(concat)

# ==================================================
# Step 5: Apply & Lambda
# ==================================================

# apply() allows custom functions across rows/columns.
# lambda provides quick inline functions.
# Use Case: Classify employees into High/Low salary.
print("\n=== Apply Lambda Example: Salary Category ===")
df_clean['Result'] = df_clean['Salary'].apply(lambda x: 'High' if x > 55000 else 'Low')
print(df_clean[['Name','Salary','Result']])

# ==================================================
# Step 6: Pivot Tables & Crosstab
# ==================================================

# pivot_table() works like Excel Pivot Table.
# Use Case: Find average salary by department.
print("\n=== Pivot Table: Avg Salary by Dept ===")
print(pd.pivot_table(df_clean, values='Salary', index='Department', aggfunc='mean'))

# crosstab() creates frequency tables.
# Use Case: Count employees per department in age groups.
print("\n=== Crosstab: Dept vs Age Groups ===")
age_bins = pd.cut(df_clean['Age'], bins=[20,30,40,50], labels=['20-30','30-40','40-50'])
print(pd.crosstab(df_clean['Department'], age_bins))

# ==================================================
# Step 7: Time-Series Handling
# ==================================================

# Convert Joining_Date to datetime for time-series analysis.
# Use Case: Count employees joined per year.
print("\n=== Convert Joining_Date to Datetime ===")
df_clean['Joining_Date'] = pd.to_datetime(df_clean['Joining_Date'])
print(df_clean[['Name','Joining_Date']])

print("\n=== Resample: Employees Joined per Year ===")
df_clean.set_index('Joining_Date', inplace=True)
print(df_clean.resample('Y')['Name'].count())

# ==================================================
# Step 8: Advanced Indexing (MultiIndex)
# ==================================================

# MultiIndex allows multiple levels of indexing.
# Use Case: Store exam results for multiple tests per department.
arrays = [
    ['HR', 'HR', 'IT', 'Finance'],
    ['Test1', 'Test2', 'Test1', 'Test1']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Department','Exam'))
scores = pd.Series([85, 88, 90, 75], index=index)

print("\n=== MultiIndex Example ===")
print(scores)

# ==================================================
# Step 9: Performance Optimization
# ==================================================

# Vectorization applies operations on entire columns, faster than loops.
# Use Case: Calculate Bonus for all employees at once.
print("\n=== Vectorization Example: Bonus Calculation ===")
df_clean['Bonus'] = df_clean['Salary'] * 0.10
print(df_clean[['Salary','Bonus']])

# Categorical data reduces memory usage for repetitive strings.
# Use Case: Optimize Department column.
print("\n=== Convert Department to Categorical ===")
df_clean['Department'] = df_clean['Department'].astype('category')
print(df_clean.dtypes)
