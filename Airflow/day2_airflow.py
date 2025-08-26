# Import necessary libraries
from __future__ import annotations

import pendulum
import pandas as pd
import mysql.connector

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

# --- 1. Define Python Functions for Tasks ---

def extract_data() -> str:
    """
    Connects to the MySQL database, extracts the first 100 records from the
    'account' table, and returns the data as a JSON string.
    This JSON string is automatically pushed to Airflow's XCom.
    """
    print("Starting data extraction...")
    try:
        # Establish a connection to the database
        # BEST PRACTICE: Use Airflow Connections to store credentials.
        mydb = mysql.connector.connect(
            host="nonprod.cluster-cprsywmazgvp.ap-southeast-1.rds.amazonaws.com",
            user="sg_internal",
            password="m8Y5MjUh7SB%g",
            port=3306,
            database="ccbuser"
        )
        print("✅ Successfully connected to MySQL database.")

        # Define the SQL query to fetch 100 records
        query = "SELECT * FROM account LIMIT 100"

        # Use pandas to execute the query and load data into a DataFrame
        df = pd.read_sql(query, mydb)
        print(f"✅ Extracted {len(df)} records from the database.")

        # Return DataFrame as a JSON string to pass to the next task via XCom
        return df.to_json()

    except Exception as e:
        print(f"❌ Error during data extraction: {e}")
        raise
    finally:
        # Ensure the database connection is closed
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")


def load_data(data_json: str):
    """
    Receives data as a JSON string (from XCom), converts it back to a
    pandas DataFrame, and writes it to a local CSV file.
    """
    print("Starting data loading process...")
    output_path = "/tmp/account_file.csv" # Standard temp directory in Airflow workers

    # Convert the JSON string back to a pandas DataFrame
    df = pd.read_json(data_json)

    # Write the DataFrame to a CSV file in the local filesystem
    df.to_csv(output_path, index=False)
    print(f"✅ Successfully wrote {len(df)} records to {output_path}")


# --- 2. Define the Airflow DAG ---

with DAG(
    dag_id="mysql_to_local_csv_pipeline",
    start_date=pendulum.datetime(2025, 8, 26, tz="UTC"),
    schedule=None,  # This DAG runs only when triggered manually
    catchup=False,
    doc_md="A simple DAG to extract 100 records from MySQL and save to a local CSV file.",
    tags=["mysql", "pandas", "local_file"],
) as dag:
    # --- 3. Define the Tasks ---

    extract_data_task = PythonOperator(
        task_id="extract_data_from_mysql",
        python_callable=extract_data,
    )

    load_data_to_file_task = PythonOperator(
        task_id="load_data_to_local_file",
        python_callable=load_data,
        # Pass the output of the previous task as an argument
        op_kwargs={"data_json": "{{ task_instance.xcom_pull(task_ids='extract_data_from_mysql') }}"}
    )

    # --- 4. Set Task Dependencies ---
    # This means `extract_data_task` must complete successfully
    # before `load_data_to_file_task` can start.
    extract_data_task >> load_data_to_file_task