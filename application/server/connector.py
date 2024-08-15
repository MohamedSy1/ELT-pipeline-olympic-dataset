import os
import snowflake.connector
from dotenv import load_dotenv
import pandas

load_dotenv()

PASSWORD = os.getenv('SNOWSQL_PWD')
WAREHOUSE = os.getenv('WAREHOUSE')
ACCOUNT = os.getenv('ACCOUNT')

conn = snowflake.connector.connect(
    user='MOHSY1',
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database='OLYMPICTOKYO',
    schema='DBT_SCHEMA'
    )


dimOlympics = conn.cursor().execute("SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_OLYMPICS")
dimOlympics.fetch_pandas_all().to_csv("./views/dim_olympics.csv")
