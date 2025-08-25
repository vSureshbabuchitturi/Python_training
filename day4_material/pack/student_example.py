# ============================
# Pandas Student Tasks with Descriptions
# ============================

import pandas as pd

# ----------------------------
# Task 1: Install & Import Pandas
# ----------------------------
# Pandas is a library for data manipulation & analysis.
# Installation: pip install pandas openpyxl
# openpyxl is needed for Excel support.
import pandas as pd


# ----------------------------
# Task 2: Create DataFrame from Dictionary
# ----------------------------
# DataFrame is a 2D tabular data structure in Pandas (rows + columns).
# You can create it from dict, list of dicts, list of tuples, etc.
data = {
    "Roll Number": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 90, 78, 88, 92],
    "Science": [80, 95, 75, 85, 89]
}
df = pd.DataFrame(data)
print("\n=== DataFrame from Dictionary ===")
print(df)


# ----------------------------
# Task 3: Load Data from CSV
# ----------------------------
# pd.read_csv("file.csv") → Reads a CSV file into a DataFrame.
df = pd.read_csv("marks.csv")
print("\n=== First 5 Rows from CSV ===")
print(df.head())   # head() shows first 5 rows by default


# ----------------------------
# Task 4: Show First 10 Rows
# ----------------------------
# df.head(n) → Shows first n rows
print("\n=== First 10 Rows ===")
print(df.head(10))


# ----------------------------
# Task 5: Shape, Info, Describe
# ----------------------------
# df.shape → returns (rows, columns)
# df.info() → data types + memory usage + null count
# df.describe() → summary statistics (mean, std, min, max, quartiles)
print("\n=== Shape of Data ===")
print(df.shape)

print("\n=== Info ===")
print(df.info())

print("\n=== Summary Statistics ===")
print(df.describe())


# ----------------------------
# Task 6: Select 'Name' Column
# ----------------------------
# df["col_name"] → selects a single column (returns Series).
print("\n=== Name Column ===")
print(df["Name"].head())


# ----------------------------
# Task 7: Select Roll Number & Name
# ----------------------------
# df[["col1","col2"]] → selects multiple columns (returns DataFrame).
print("\n=== Roll Number & Name ===")
print(df[["Roll Number", "Name"]].head())


# ----------------------------
# Task 8: Select Rows with loc
# ----------------------------
# loc → label-based selection.
# Syntax: df.loc[row_index, column_labels]
# Example: df.loc[0:4] → rows 0 to 4 (inclusive).
print("\n=== First 5 Rows using loc ===")
print(df.loc[0:4])


# ----------------------------
# Task 9: Select Rows/Cols with iloc
# ----------------------------
# iloc → integer-position-based selection.
# Syntax: df.iloc[row_index, column_index]
# Example: df.iloc[0:3, 0:2] → first 3 rows and first 2 columns.
print("\n=== First 3 Rows & 2 Columns using iloc ===")
print(df.iloc[0:3, 0:2])


# ----------------------------
# Task 10: Sort by Total Marks
# ----------------------------
# df.sort_values(by="col", ascending=True/False) → sorts data.
df["Total"] = df[["Maths", "Science", "English", "History", "Geography"]].sum(axis=1)
sorted_df = df.sort_values(by="Total", ascending=False)
print("\n=== Top 5 Students by Total Marks ===")
print(sorted_df.head())


# ----------------------------
# Task 11: Add Grade Column
# ----------------------------
# df["new_col"] = values → adds a new column.
# apply(function) → applies a function to each element/row.
def grade(marks):
    if marks >= 450:
        return "A"
    elif marks >= 400:
        return "B"
    else:
        return "C"

df["Grade"] = df["Total"].apply(grade)
print("\n=== Students with Grades ===")
print(df[["Name", "Total", "Grade"]].head())


# ----------------------------
# Task 12: Drop 'Grade' Column
# ----------------------------
# df.drop("col", axis=1) → drops a column
# inplace=True → updates original DataFrame instead of returning new one
df = df.drop("Grade", axis=1)
print("\n=== Data after Dropping Grade Column ===")
print(df.head())


# ----------------------------
# Task 13: Handle Missing Data
# ----------------------------
# df.fillna(value) → fills NaN with given value/mean/median/mode
# df.dropna() → removes rows with NaN values
df_missing = pd.read_excel("marks.xlsx", sheet_name="marks_with_missing_data")
df_filled = df_missing.fillna(df_missing.mean(numeric_only=True))  # Fill with mean
df_dropped = df_missing.dropna()  # Drop rows with NaN
print("\n=== Missing Data Handled (Filled with Mean) ===")
print(df_filled.head())


# ----------------------------
# Task 14: Remove Duplicates
# ----------------------------
# df.drop_duplicates() → removes duplicate rows
df_dup = pd.read_excel("marks.xlsx", sheet_name="marks_with_duplicates")
cleaned_df = df_dup.drop_duplicates()
print("\n=== After Removing Duplicates ===")
print(cleaned_df.shape)


# ----------------------------
# Task 15: Export Cleaned Data to CSV
# ----------------------------
# df.to_csv("file.csv", index=False) → saves DataFrame to CSV
cleaned_df.to_csv("cleaned_marks.csv", index=False)


# ----------------------------
# Task 16: Export Cleaned Data to Excel (Multiple Sheets)
# ----------------------------
# pd.ExcelWriter("file.xlsx") → allows writing multiple sheets in one file
with pd.ExcelWriter("cleaned_marks.xlsx") as writer:
    df_filled.to_excel(writer, sheet_name="missing_filled", index=False)
    cleaned_df.to_excel(writer, sheet_name="duplicates_removed", index=False)


# ----------------------------
# Task 17: Share Screenshots of Outputs
# ----------------------------
# Not code – but in Jupyter/VS Code, take screenshots of each output
