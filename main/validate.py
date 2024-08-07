#!/usr/bin/env python
import snowflake.connector
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType


load_dotenv()

# Gets the version
ctx = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    session_parameters={
        'QUERY_TAG': '2021OlympicTransformation'
    }
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()


ctx.cursor().execute("USE DATABASE OLYMPICTOKYO")

output_dir = "../data/"

def fetch_data_to_df(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    return df

athletes_df = fetch_data_to_df(ctx.cursor(), 'SELECT * FROM ATHLETES')
coaches_df = fetch_data_to_df(ctx.cursor(), 'SELECT * FROM COACHES')
entriesgender_df = fetch_data_to_df(ctx.cursor(), 'SELECT * FROM ENTRIESGENDER')
medals_df = fetch_data_to_df(ctx.cursor(), 'SELECT * FROM MEDALS')
teams_df = fetch_data_to_df(ctx.cursor(), 'SELECT * FROM TEAMS')

os.makedirs(output_dir, exist_ok=True)

athletes_df.to_csv(os.path.join(output_dir, 'athletes.csv'), index=False)
coaches_df.to_csv(os.path.join(output_dir, 'coaches.csv'), index=False)
entriesgender_df.to_csv(os.path.join(output_dir, 'entriesgender.csv'), index=False)
medals_df.to_csv(os.path.join(output_dir, 'medals.csv'), index=False)
teams_df.to_csv(os.path.join(output_dir, 'teams.csv'), index=False)


ctx.close()