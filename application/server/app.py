import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from flask import Flask, jsonify, request
from flask_cors import CORS
from tempfile import NamedTemporaryFile
from langchain_openai import OpenAI
import re
import csv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

load_dotenv()

# Read OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY must be set in .env file")

@app.route('/predict', methods=['POST'])

def predict():
    csv_file_path = "./views/dim_olympics.csv"

    if not os.path.exists(csv_file_path):
        return jsonify({'error': 'CSV file not found'}), 404
    
  
    agent = create_csv_agent(
        OpenAI(api_key=openai_api_key, temperature=0),
        csv_file_path,
        verbose=True,
        encoding='utf-8',
        allow_dangerous_code=True
    )

    question = request.form['question']

    result = agent.run(question)

    return jsonify({'result': result})

if __name__ == '__main__':
  app.run(debug=True)
