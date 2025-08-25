# ================================================================
# Python + Pandas + Database Training Script
# Covers: sys.argv, CSV, JSON, SQLite, Pandas, ETL Pipeline
# ================================================================

# ------------------------------------------------
# 1. Command-line Arguments (sys.argv)
# ------------------------------------------------
import sys

if len(sys.argv) > 1:   # Only run if argument is passed
    filename = sys.argv[1]
    with open(filename, "r") as f:
        text = f.read()
    words = text.split()
    print("\n=== Command-line Example ===")
    print(f"File: {filename}")
    print(f"Total words: {len(words)}")
else:
    print("\nNo command-line argument passed. Skipping word counter...")

# ------------------------------------------------
# 2. Working with CSV using Pandas
# ------------------------------------------------
import pandas as pd

print("\n=== CSV Example ===")
df = pd.read_csv("marks.csv")   # Make sure marks.csv exists
print("First 5 rows:\n", df.head())
print("\nMean values:\n", df.mean(numeric_only=True))
print("\nMax values:\n", df.max(numeric_only=True))
print("\nMin values:\n", df.min(numeric_only=True))

# ------------------------------------------------
# 3. Working with JSON
# ------------------------------------------------
import json

print("\n=== JSON Example ===")
# Example file: students.json → {"students":[{"id":1,"name":"Alice","age":20},{"id":2,"name":"Bob","age":21}]}
try:
    with open("students.json", "r") as f:
        data = json.load(f)

    for student in data["students"]:
        print("ID:", student["id"], "| Name:", student["name"], "| Age:", student["age"])
except FileNotFoundError:
    print("students.json file not found, skipping JSON example...")

# ------------------------------------------------
# 4. Database Connectivity – Insert Data
# ------------------------------------------------
import sqlite3

print("\n=== Database Insert Example ===")
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    dept TEXT,
                    salary REAL)""")

employees = [
    (1, "Alice", "HR", 50000),
    (2, "Bob", "IT", 60000),
    (3, "Charlie", "Finance", 70000),
]

cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)", employees)
conn.commit()
print("Inserted employee records into database.")

# ------------------------------------------------
# 5. Database → Pandas DataFrame
# ------------------------------------------------
print("\n=== Database to Pandas Example ===")
df_emp = pd.read_sql_query("SELECT * FROM employees", conn)
print(df_emp)

df_emp.to_csv("employees_export.csv", index=False)
print("Exported employees to employees_export.csv")

# ------------------------------------------------
# 6. ETL Pipeline: CSV → SQL → Pandas
# ------------------------------------------------
print("\n=== ETL Pipeline Example ===")

# Step 1: Extract (Read CSV)
marks = pd.read_csv("marks.csv")
print("Extracted CSV data")

# Step 2: Load (Insert into SQL)
marks.to_sql("marks", conn, if_exists="replace", index=False)
print("Loaded data into SQL table")

# Step 3: Transform (Analyze with Pandas)
df_marks = pd.read_sql_query("SELECT * FROM marks", conn)
print("\nAverage per subject:\n", df_marks.mean(numeric_only=True))
print("\nTop Scorer (by Maths):\n", df_marks.loc[df_marks['Maths'].idxmax()])

conn.close()

# ================================================================
# End of Script
# ================================================================
