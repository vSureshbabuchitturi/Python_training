# ================================================================
# MySQL CRUD Operations with Python (mysql.connector)
# ================================================================
import mysql.connector

# ------------------------------------------------
# Connect to MySQL Database
# ------------------------------------------------
mydb = mysql.connector.connect(
    host="nonprod.cluster-cprsywmazgvp.ap-southeast-1.rds.amazonaws.com",  
    user="sg_internal",
    password="m8Y5MjUh7SB%g",
    port="3306",
    database="ccbuser"
)

mycursor = mydb.cursor()

# ------------------------------------------------
# Create Table (if not exists)
# ------------------------------------------------
mycursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2)
)
""")
print("Table created successfully!")

# ------------------------------------------------
# 1. CREATE (Insert Records)
# ------------------------------------------------
print("\n=== CREATE Records ===")
sql = "INSERT INTO employees (name, dept, salary) VALUES (%s, %s, %s)"
values = [
    ("Alice", "HR", 50000),
    ("Bob", "IT", 60000),
    ("Charlie", "Finance", 70000)
]
mycursor.executemany(sql, values)
mydb.commit()
print(mycursor.rowcount, "records inserted.")

# ------------------------------------------------
# 2. READ (Select Records)
# ------------------------------------------------
print("\n=== READ Records ===")
mycursor.execute("SELECT * FROM employees")
rows = mycursor.fetchall()
for row in rows:
    print(row)

# ------------------------------------------------
# 3. UPDATE (Modify Records)
# ------------------------------------------------
print("\n=== UPDATE Record ===")
update_sql = "UPDATE employees SET salary = %s WHERE name = %s"
mycursor.execute(update_sql, (65000, "Bob"))
mydb.commit()
print("Updated Bob's salary.")

mycursor.execute("SELECT * FROM employees")
for row in mycursor.fetchall():
    print(row)

# ------------------------------------------------
# 4. DELETE (Remove Records)
# ------------------------------------------------
print("\n=== DELETE Record ===")
delete_sql = "DELETE FROM employees WHERE name = %s"
mycursor.execute(delete_sql, ("Charlie",))
mydb.commit()
print("Deleted Charlie's record.")

mycursor.execute("SELECT * FROM employees")
for row in mycursor.fetchall():
    print(row)

# ------------------------------------------------
# Close Connection
# ------------------------------------------------
mycursor.close()
mydb.close()
print("\nDatabase connection closed.")
