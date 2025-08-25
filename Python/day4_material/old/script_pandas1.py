# ==============================================
# Step 1: Import pandas
# ==============================================
# Pandas is the main library we use for data analysis in Python.
# We import it using the alias 'pd' which is a common convention.
import pandas as pd

# ==============================================
# Step 2: Series Example
# ==============================================
# A Series is like a single column in Excel. 
# It has values and an index (labels).
print("\n=== Pandas Series Example ===")
marks = pd.Series([85, 90, 78], index=['Math', 'Science', 'English'])
print(marks)

# ==============================================
# Step 3: DataFrame Example
# ==============================================
# A DataFrame is like a full Excel sheet or SQL table. 
# It contains rows and multiple columns.

print("\n=== DataFrame Example ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Marks': [85, 90, 78, 88, 95],
    'Department': ['Math', 'Science', 'English', 'Math', 'Science']
}

df = pd.DataFrame(data)
print(df)

# ==============================================
# Step 4: Writing Data (Create students.csv)
# ==============================================
# First we save our DataFrame to a CSV file. 
# This will create 'students.csv' so we can use it for reading examples.
df.to_csv("students.csv", index=False)
print("\nstudents.csv file created successfully!")

# ==============================================
# Step 5: Reading Data from CSV
# ==============================================
# Now we read the 'students.csv' file back into a new DataFrame.
# This simulates reading external data for analysis.
students = pd.read_csv("students.csv")
print("\n=== Reading Data from students.csv (first 3 rows) ===")
print(students.head(3))   # first 3 rows

# ==============================================
# Step 6: Writing Data (Save to CSV & Excel)
# ==============================================
# We can save data in multiple formats like CSV and Excel.
#pip install openpyxl

df.to_csv("students_output.csv", index=False)
df.to_excel("students_output.xlsx", index=False)
print("\nData saved to CSV (students_output.csv) and Excel (students_output.xlsx) successfully.")

# ==============================================
# Step 7: Filtering Data
# ==============================================
# Filtering allows us to select rows based on conditions.
# Example: Find students with Marks > 85.
print("\n=== Filtering Data: Marks > 85 ===")
high_scores = df[df['Marks'] > 85]
print(high_scores)

# Multiple conditions: Department = Science AND Age < 30
print("\n=== Filtering Data: Science Dept and Age < 30 ===")
science_young = df[(df['Department'] == 'Science') & (df['Age'] < 30)]
print(science_young)

# ==============================================
# Step 8: Sorting Data
# ==============================================
# Sorting lets us arrange rows by one or more columns.
print("\n=== Sorting by Marks (Descending) ===")
sorted_marks = df.sort_values(by='Marks', ascending=False)
print(sorted_marks)

# Sorting by multiple columns: First by Department, then Age
print("\n=== Sorting by Department, then Age ===")
sorted_dept = df.sort_values(by=['Department', 'Age'])
print(sorted_dept)

# ==============================================
# Step 9: Describe Data (Quick Stats)
# ==============================================
# describe() gives quick statistics like mean, min, max, std etc.
print("\n=== Describe Data ===")
print(df.describe())

# ==============================================
# Step 10: Practice Tasks
# ==============================================
# These are exercises for students to try themselves.

# 1. Filter all students from Math department with Marks > 80
print("\nTask 1: Math Dept with Marks > 80")
task1 = df[(df['Department'] == 'Math') & (df['Marks'] > 80)]
print(task1)

# 2. Sort students by Age ascending, then Marks descending
print("\nTask 2: Sort by Age Asc, Marks Desc")
task2 = df.sort_values(by=['Age', 'Marks'], ascending=[True, False])
print(task2)

# 3. Save only Name and Marks to a new CSV file
print("\nTask 3: Save Name & Marks to new CSV")
df[['Name', 'Marks']].to_csv("name_marks.csv", index=False)
print("File 'name_marks.csv' created.")

# 4. Use describe() to check average Age and Marks
print("\nTask 4: Average Age and Marks")
print(df[['Age', 'Marks']].describe())
