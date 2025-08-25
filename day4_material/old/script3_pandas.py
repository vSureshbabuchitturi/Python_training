import pandas as pd

# Create sample DataFrame
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)
#1.How to select only one column?
#How to select multiple columns at once?
# Select one column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Salary"]])

# Save to Excel
df.to_excel("employees.xlsx", index=False)

print("employees.xlsx file created!")
print("Now reading data from excel")
df_excel = pd.read_excel("employees.xlsx")
print(df_excel)

#iloc in Pandas
#iloc stands for integer-location based indexing.
#It is used to select rows and columns by their position (index number), not by label.
# Think of it as:
# iloc = "pick by number"
#loc = "pick by name/label"

#Now Select Rows by Position

print("Select Rows by Position")
print(df.iloc[0])      # First row
print(df.iloc[1])      # Second row
print(df.iloc[-1])     # Last row

#Select Rows + Columns
print(df.iloc[0, 1])       # Row 0, Column 1 → "Alice"
print(df.iloc[2, 2])       # Row 2, Column 2 → 28

#Avoid Printing dtype: object
#Convert to Dictionary
print("from dictionay")
print(df.iloc[0].to_dict())

#Convert to List
print("from list")
print(df.iloc[0].tolist())

#3. Filtering with Conditions
# Employees with Age > 25
print(df[df["Age"] > 25])

# Employees with Salary >= 55000
print(df[df["Salary"] >= 55000])

# Multiple conditions (AND)
print(df[(df["Age"] > 25) & (df["Salary"] > 55000)])

#try 
print("From start")
print(df.head(2))

#from last 
print("From last")

print(df.tail(2))




