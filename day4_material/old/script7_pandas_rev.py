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
print("\n=== Fill Missing Salary with Mean (fillna) ===")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)

# --- dropna() ---
print("\n=== Drop Rows with Missing Age (dropna) ===")
df_clean = df.dropna(subset=['Age']).copy()  # ✅ use .copy() to avoid warning
print(df_clean)

# --- drop_duplicates() ---
print("\n=== Remove Duplicate Rows (drop_duplicates) ===")
print(df_clean.drop_duplicates())

# ==================================================
# Step 3: Grouping & Aggregation
# ==================================================
print("\n=== Average Salary per Department ===")
print(df_clean.groupby('Department')['Salary'].mean())

print("\n=== Count Employees per Department ===")
print(df_clean.groupby('Department')['Name'].count())

# ==================================================
# Step 4: Merging & Joining
# ==================================================
df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame({'ID':[1,2,3], 'Marks':[85,90,78]})

print("\n=== Merge Example (SQL-like JOIN) ===")
merged = pd.merge(df1, df2, on='ID')
print(merged)

print("\n=== Concat Example (Stack Vertically) ===")
concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(concat)

# ==================================================
# Step 5: Apply & Lambda
# ==================================================
print("\n=== Apply Lambda Example: Salary Category ===")
df_clean.loc[:, 'Result'] = df_clean['Salary'].apply(lambda x: 'High' if x > 55000 else 'Low')  # ✅ use .loc
print(df_clean[['Name','Salary','Result']])

# ==================================================
# Step 6: Pivot Tables & Crosstab
# ==================================================
print("\n=== Pivot Table: Avg Salary by Dept ===")
print(pd.pivot_table(df_clean, values='Salary', index='Department', aggfunc='mean'))

print("\n=== Crosstab: Dept vs Age Groups ===")
age_bins = pd.cut(df_clean['Age'], bins=[20,30,40,50], labels=['20-30','30-40','40-50'])
print(pd.crosstab(df_clean['Department'], age_bins))

# ==================================================
# Step 7: Time-Series Handling
# ==================================================
print("\n=== Convert Joining_Date to Datetime ===")
df_clean.loc[:, 'Joining_Date'] = pd.to_datetime(df_clean['Joining_Date'])  # ✅ use .loc
print(df_clean[['Name','Joining_Date']])

print("\n=== Resample: Employees Joined per Year ===")
df_clean = df_clean.set_index('Joining_Date')  # ✅ assign back to df_clean
print(df_clean.resample('Y')['Name'].count())

# ==================================================
# Step 8: Advanced Indexing (MultiIndex)
# ==================================================
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
print("\n=== Vectorization Example: Bonus Calculation ===")
df_clean.loc[:, 'Bonus'] = df_clean['Salary'] * 0.10  # ✅ use .loc
print(df_clean[['Salary','Bonus']])

print("\n=== Convert Department to Categorical ===")
df_clean.loc[:, 'Department'] = df_clean['Department'].astype('category')  # ✅ use .loc
print(df_clean.dtypes)
