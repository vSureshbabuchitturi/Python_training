# ================================================================
# Python + SQLite3 CRUD Operations
# ================================================================
import sqlite3
import pandas as pd

# ------------------------------------------------
# Connect to DB (Create if not exists)
# ------------------------------------------------
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept TEXT,
    salary REAL
)
""")
conn.commit()

# ------------------------------------------------
# 1. CREATE (Insert Records)
# ------------------------------------------------
print("\n=== CREATE Records ===")
employees = [
    (1, "Alice", "HR", 50000),
    (2, "Bob", "IT", 60000),
    (3, "Charlie", "Finance", 70000),
]

cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)", employees)
conn.commit()
print("Inserted records successfully.")

# ------------------------------------------------
# 2. READ (Select Records)
# ------------------------------------------------
print("\n=== READ Records ===")
df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)

# ------------------------------------------------
# 3. UPDATE (Modify Records)
# ------------------------------------------------
print("\n=== UPDATE Records ===")
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (65000, "Bob"))
conn.commit()

df = pd.read_sql_query("SELECT * FROM employees", conn)
print("After Update:\n", df)

# ------------------------------------------------
# 4. DELETE (Remove Records)
# ------------------------------------------------
print("\n=== DELETE Records ===")
cursor.execute("DELETE FROM employees WHERE name = ?", ("Charlie",))
conn.commit()

df = pd.read_sql_query("SELECT * FROM employees", conn)
print("After Delete:\n", df)

# ------------------------------------------------
# 5. CLEANUP / Close
# ------------------------------------------------
conn.close()
print("\nDatabase connection closed.")
