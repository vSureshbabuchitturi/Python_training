# ================================================================
# SQLite3 CRUD Operations in Python (Without Pandas)
# ================================================================
import sqlite3

# ------------------------------------------------
# Connect to Database (creates if not exists)
# ------------------------------------------------
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# ------------------------------------------------
# Create Table
# ------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary REAL
)
""")
conn.commit()
print("Table created successfully!")

# ------------------------------------------------
# 1. CREATE (Insert Records)
# ------------------------------------------------
print("\n=== CREATE Records ===")
cursor.execute("INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)", 
               ("Alice", "HR", 50000))
cursor.execute("INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)", 
               ("Bob", "IT", 60000))
cursor.execute("INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)", 
               ("Charlie", "Finance", 70000))
conn.commit()
print("Inserted records successfully.")

# ------------------------------------------------
# 2. READ (Select Records)
# ------------------------------------------------
print("\n=== READ Records ===")
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ------------------------------------------------
# 3. UPDATE (Modify Records)
# ------------------------------------------------
print("\n=== UPDATE Record ===")
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (65000, "Bob"))
conn.commit()
print("Updated Bob's salary.")

cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------
# 4. DELETE (Remove Records)
# ------------------------------------------------
print("\n=== DELETE Record ===")
cursor.execute("DELETE FROM employees WHERE name = ?", ("Charlie",))
conn.commit()
print("Deleted Charlie's record.")

cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------
# Close Connection
# ------------------------------------------------
conn.close()
print("\nDatabase connection closed.")




"""
cursor.execute() → Executes SQL commands.

? placeholders → Prevent SQL injection (safer queries).

conn.commit() → Saves changes (important after INSERT/UPDATE/DELETE).

fetchall() → Retrieves query results.



"""