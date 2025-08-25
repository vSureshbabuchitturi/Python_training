import mysql.connector
import pandas as pd
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
mycursor.execute('select * from account_status')
#dataframe = pd.DataFrame(mycursor.fetchall())
rows = mycursor.fetchall()

# Get column names
columns = [column[0] for column in mycursor.description]

# Create DataFrame
df = pd.DataFrame.from_records(rows, columns=columns)

print(df.head())
print(df.columns.tolist())  # headers