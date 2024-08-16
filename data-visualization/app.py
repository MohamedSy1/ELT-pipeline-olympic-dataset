import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import snowflake.connector
from dotenv import load_dotenv
import pandas

load_dotenv()

st.title("What happened in tokyo 2021 olympics")
st.sidebar.title("Analysis of the tokyo 2021 olympics")
st.markdown("this application is a streamlit app used to analyze tokyo 2021 olympics")

PASSWORD = os.getenv('PASSWORD')
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
