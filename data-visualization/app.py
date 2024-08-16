import os
import streamlit as st
import pandas as pd
import plotly.express as px
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit App Title and Sidebar
st.title("What happened in Tokyo 2021 Olympics")
st.sidebar.title("Analysis of the Tokyo 2021 Olympics")
st.markdown("This application is a Streamlit app used to analyze the Tokyo 2021 Olympics")

# Snowflake connection details
PASSWORD = os.getenv('PASSWORD')
WAREHOUSE = os.getenv('WAREHOUSE')
ACCOUNT = os.getenv('ACCOUNT')

# Establish connection to Snowflake
conn = snowflake.connector.connect(
    user='MOHSY1',
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database='OLYMPICTOKYO',
    schema='DBT_SCHEMA'
)

# Function to fetch data from Snowflake
def fetch_data(query):
    return pd.read_sql(query, conn)

# Queries for each table
queries = {
    "DIM_COACHES_IN_BASKETBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_COACHES_IN_BASKETBALL",
    "DIM_COACHES_IN_FOOTBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_COACHES_IN_FOOTBALL",
    "DIM_COACHES_IN_HANDBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_COACHES_IN_HANDBALL",
    "DIM_COACHES_IN_VOLLEYBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_COACHES_IN_VOLLEYBALL",
    "DIM_OLYMPICS": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_OLYMPICS",
    "DIM_TOTAL_COACHES": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_TOTAL_COACHES",
    "DIM_TOTAL_TEAMS": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_TOTAL_TEAMS",
    "DIM_OLYMPIC_GAMES_WITH_MOST_ATHLETE": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_OLYMPIC_GAMES_WITH_MOST_ATHLETE",
    "DIM_WOMEN_PARTICIPATE_BASKETBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_WOMEN_PARTICIPATE_BASKETBALL",
    "DIM_WOMEN_PARTICIPATE_FOOTBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_WOMEN_PARTICIPATE_FOOTBALL",
    "DIM_WOMEN_PARTICIPATE_HANDBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_WOMEN_PARTICIPATE_HANDBALL",
    "DIM_WOMEN_PARTICIPATE_VOLLEYBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_WOMEN_PARTICIPATE_VOLLEYBALL",
    "DIM_MEN_PARTICIPATE_BASKETBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_MEN_PARTICIPATE_BASKETBALL",
    "DIM_MEN_PARTICIPATE_HANDBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_MEN_PARTICIPATE_HANDBALL",
    "DIM_MEN_PARTICIPATE_VOLLEYBALL": "SELECT * FROM OLYMPICTOKYO.DBT_SCHEMA.DIM_MEN_PARTICIPATE_VOLLEYBALL"
}

# Fetch data for all tables
dataframes = {name: fetch_data(query) for name, query in queries.items()}

# Display Data in Streamlit
st.sidebar.subheader("Select a Table to View")
table_selection = st.sidebar.selectbox('Choose a Table', list(dataframes.keys()))

# Display the selected table
st.write(f"### Data from {table_selection} Table")
st.dataframe(dataframes[table_selection])

# Optionally, add visualizations or other analyses below
if st.sidebar.checkbox("Show Visualizations"):
    if table_selection in dataframes:
        df = dataframes[table_selection]
        if 'TEAM_COUNTRY' in df.columns:
            st.write("### Number of Teams by Country")
            fig = px.histogram(df, x='TEAM_COUNTRY', title=f'Number of Teams by Country in {table_selection}')
            st.plotly_chart(fig)
        elif 'NUM_COACHES' in df.columns:
            st.write("### Number of Coaches by Country")
            fig = px.bar(df, x='COACH_COUNTRY', y='NUM_COACHES', title=f'Number of Coaches by Country in {table_selection}')
            st.plotly_chart(fig)
        # Add more visualizations as needed based on the columns in the selected table

# Close the connection
conn.close()
