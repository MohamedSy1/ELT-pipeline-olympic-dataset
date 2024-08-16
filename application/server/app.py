import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from flask import Flask, jsonify, request
from flask_cors import CORS
from tempfile import NamedTemporaryFile
from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from sqlalchemy import create_engine, inspect
import urllib.parse
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=openai_api_key,
    organization='org-MnKIQ4i1PLLDFPPdwl8GtvAM',
)

@app.route('/predict', methods=['POST'])
def predict():
    if openai_api_key is None:
        raise ValueError("OPENAI_API_KEY must be set in .env file")

    USER_DBT = os.getenv("USER_dbt")
    PASSWORD = os.getenv("PASSWORD")
    ACCOUNT = os.getenv('ACCOUNT')
    SCHEMA = os.getenv('DBT_SCHEMA')
    DATABASE = os.getenv('DATABASE')
    WAREHOUSE = os.getenv('WAREHOUSE')

    encoded_password = urllib.parse.quote_plus(PASSWORD)

    # Construct the connection string for Snowflake
    connection_string = f'snowflake://{USER_DBT}:{encoded_password}@{ACCOUNT}/{DATABASE}/{SCHEMA}?warehouse={WAREHOUSE}'

    db = SQLDatabase.from_uri(connection_string, sample_rows_in_table_info=1, include_tables=['dim_medal_count_athlete_count', 'dim_most_participants_by_country', 'dim_olympics'])

    execute_query = QuerySQLDataBaseTool(db=db)
    write_query = create_sql_query_chain(client, db)

    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
    )

    chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | answer_prompt
        | client
        | StrOutputParser()
    )

    question = request.form['question']
    result = chain.invoke({"question": question})

    return jsonify({'result': result})

if __name__ == '__main__':
  app.run(debug=True)