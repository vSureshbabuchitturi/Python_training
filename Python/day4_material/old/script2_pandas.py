import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# Step 1: Create Sample Sales Data
# ==================================================
print("=== Sales Data ===")
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales_A': [250, 300, 400, 350, 500],
    'Sales_B': [200, 280, 320, 300, 450]
}
df = pd.DataFrame(data)
print(df)

# ==================================================
# Step 2: Summary Statistics
# ==================================================
print("\n=== Summary Statistics ===")
print(df.describe())

# ==================================================
# Step 3: Line Plot (Sales Trend)
# ==================================================
# Line charts are useful for showing trends over time.
plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales_A'], marker='o', label='Store A')
plt.plot(df['Month'], df['Sales_B'], marker='o', label='Store B')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# ==================================================
# Step 4: Bar Chart (Comparing Sales per Month)
# ==================================================
# Bar charts are used for comparing categories side by side.
df.plot(x='Month', kind='bar', figsize=(8,5))
plt.title("Sales Comparison (Bar Chart)")
plt.ylabel("Sales")
plt.show()

# ==================================================
# Step 5: Pie Chart (Total Sales Share)
# ==================================================
# Pie charts show proportion of total sales.
total_sales = [df['Sales_A'].sum(), df['Sales_B'].sum()]
labels = ['Store A', 'Store B']

plt.figure(figsize=(6,6))
plt.pie(total_sales, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Total Sales Share")
plt.show()
