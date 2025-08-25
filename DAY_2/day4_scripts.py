#Json
# import json
#
# data={
#   "product": {
#     "id": "PROD001",
#     "name": "Laptop",
#     "price": 1200.00,
#     "details": {
#       "brand": "TechCo",
#       "model": "XPS 15",
#       "storageGB": 512
#     }
#   }
# }
# with open('data.json', 'w+') as fo:
#     json.dump(data, fo)
# with open('data.json') as fo:
#     data = json.load(fo)
#     print(data)

#Pandas
# import pandas as pd
#
# data = {
#     "RollNo": [1, 2, 3],
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Percentage": [85, 72, 91],
#     "Grade": ["A", "B", "A+"]
# }
# df = pd.DataFrame(data)
# df.to_csv("sample.csv", index=False)
# print("sample.csv created successfully!")
#
# df = pd.read_csv("sample.csv")
# print(df)


#
import pandas as pd
df = pd.read_csv(r"D:\EV_Python_Training\day4_material\pack\marks.csv")
#print("\n=== First 5 Rows from CSV ===")
#print(df.head())   # head() shows first 5 rows by default
#print(df.columns)
#print(df.shape)
#print(df.describe())
#print(df.info)
#print(df.aggregate)
#print(df["Name"].tail())
#print(df[["Name","Roll Number","English"]].tail())
#print(df[[]])
#print(df.loc[0:4])
#print(df.iloc[0:4,0:2])

# # Task 10: Sort by Total Marks
# # ----------------------------
# #df.sort_values(by="col", ascending=True/False) → sorts data.
# df["Total"] = df[["Maths", "Science", "English", "History", "Geography"]].sum(axis=1)
# sorted_df = df.sort_values(by="Total", ascending=False)
# # print("\n=== Top 5 Students by Total Marks ===")
# # print(sorted_df.head())
# # ----------------------------
# # Task 11: Add Grade Column
# # ----------------------------
# # df["new_col"] = values → adds a new column.
# # apply(function) → applies a function to each element/row.
# def grade(marks):
#     if marks >= 450:
#         return "A"
#     elif marks >= 400:
#         return "B"
#     else:
#         return "C"
#
# df["Grade"] = df["Total"].apply(grade)
# print("\n=== Students with Grades ===")
# print(df[["Name", "Total", "Grade"]].head())
#
# df.head()
# import pandas as pd
#
# df_missing = pd.read_excel(r"D:\EV_Python_Training\day4_material\pack\marks.xlsx", sheet_name="marks_with_missing_data")
# df_filled = df_missing.fillna(df_missing.mean(numeric_only=True))  # Fill with mean
# df_dropped = df_missing.dropna()  # Drop rows with NaN
# print("\n=== Missing Data Handled (Filled with Mean) ===")
# print(df_filled.head())
#
# # df.drop_duplicates() → removes duplicate rows
# df_dup = pd.read_excel(r"D:\EV_Python_Training\day4_material\pack\marks.xlsx", sheet_name="marks_with_duplicates")
# cleaned_df = df_dup.drop_duplicates()
# print("\n=== After Removing Duplicates ===")
# print(cleaned_df.shape)
# # pd.ExcelWriter("file.xlsx") → allows writing multiple sheets in one file
# with pd.ExcelWriter("cleaned_marks.xlsx") as writer:
#     df_filled.to_excel(writer, sheet_name="missing_filled", index=False)
#     cleaned_df.to_excel(writer, sheet_name="duplicates_removed", index=False)

#Json with dataframe
# import pandas as pd
# import json
# with open("nested.json") as fo:
#     data = json.load(fo)
# df_json = pd.json_normalize(data["product"])
# print(type(df_json))
# print(df_json)
# import traceback
# import sys
# x=int(input("enter a number1:"))
# y=input("enter a number2:")
# try:
#     result=x+y
#     print(result)
# except Exception as e:
#     # Get the traceback information
#     exc_type, exc_obj, tb = sys.exc_info()
#
#     # Extract the line number from the traceback object
#     line_number = tb.tb_lineno
#
#     print(f"An error occurred: {e}")
#     print(f"Error occurred on line: {line_number}")
# print("end of program")


# import traceback
# import sys
# try:
#     x=int(input("enter a number1:"))
#     y=int(input("enter a number2:"))
#     result=x/y
#     print(result)
# except ZeroDivisionError:# Get the traceback information
#     exc_type, exc_obj, tb = sys.exc_info()
#     # Extract the line number from the traceback object
#     line_number = tb.tb_lineno
#
#     print(f"Error occurred on line: {line_number}")
# except ValueError:
#     print("Both Inputs should be integers")
# except Exception as e:
#     # Get the traceback information
#     exc_type, exc_obj, tb = sys.exc_info()
#
#     # Extract the line number from the traceback object
#     line_number = tb.tb_lineno
#     print(f"An error occurred: {e}")
#     print(f"Error occurred on line: {line_number}")
# print("end of program")

#
# import re
# try:
#     filename=open(r'D:\EV_Python_Training\DAY_2\test.txt')
#     print(filename.read())
#
#     print(a)
# except FileNotFoundError as e:
#     print("file not found")
# except Exception as e:
#     print(e)
#Finally Block
# fo=None
# try:
#     filename=open(r'D:\EV_Python_Training\DAY_2\test.txt')
#     print(filename.read())
#     #print(a)
# except FileNotFoundError as e:
#     print("file not found")
# except Exception as e:
#     print(e)
# finally:
#     if fo is not None:
#         filename.close()


# x=int(input("Enter a number:"))
# if x<0:
#     raise ValueError("Invalid input")
# else:
#     print(f"Postive number: {x}")

#
# import mysql.connector
# import pandas as pd
# # ------------------------------------------------
# # Connect to MySQL Database
# # ------------------------------------------------
# mydb = mysql.connector.connect(
#     host="nonprod.cluster-cprsywmazgvp.ap-southeast-1.rds.amazonaws.com",
#     user="sg_internal",
#     password="m8Y5MjUh7SB%g",
#     port="3306",
#     database="ccbuser"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute('select * from account a inner join business_unit bu on a.bu_id=bu.bu_id limit 1000')
# #dataframe = pd.DataFrame(mycursor.fetchall())
# rows = mycursor.fetchall()
#
# # Get column names
# columns = [column[0] for column in mycursor.description]
# print(columns)
# # Create DataFrame
# df = pd.DataFrame.from_records(rows, columns=columns)
# #print(df.head(10))
#
# print(df[["acct_id","bu_id",'acct_status_id']].tail())
# #print(df.columns.tolist())  # headers
#
# mycursor.close()
# mydb.close()

#
# import sys
# x=sys.argv
#
# server_name=x[1]
# user_name=x[2]
# password=x[3]
# location=x[4]
#
# print(server_name,user_name,password,location)


# import mysql.connector
# import pandas as pd
# import sys
# x=sys.argv
# # ------------------------------------------------
# # Connect to MySQL Database
# # ------------------------------------------------
# mydb = mysql.connector.connect(
#     host="nonprod.cluster-cprsywmazgvp.ap-southeast-1.rds.amazonaws.com",
#     user="sg_internal",
#     password="m8Y5MjUh7SB%g",
#     port=x[1],
#     database="ccbuser"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute('select * from account_status')
# #dataframe = pd.DataFrame(mycursor.fetchall())
# rows = mycursor.fetchall()
#
# # Get column names
# columns = [column[0] for column in mycursor.description]
#
# # Create DataFrame
# df = pd.DataFrame.from_records(rows, columns=columns)
#
# print(df.head())
# print(df.columns.tolist())  # headers
