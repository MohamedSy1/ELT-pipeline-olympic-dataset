# Mo Labs - Tokyo Olympics 2021 & Historical Olympics Performance Analysis

**Group Name**  
Mo Labs

**Group Members**  
Mohamed Sy

## Project Overview

This project focuses on analyzing data from the Tokyo 2021 Olympics and historical Olympic performance. The primary objectives are to:

- Identify trends in Olympic participation and performance.
- Answer key questions related to athlete and country performance.
- Provide insights into the impact of hosting the Olympics on a nation's performance.

Iemploy the ELT (Extract, Load, Transform) process, using multiple CSV files as data sources. The data is loaded into a Snowflake Warehouse, transformed using dbt Cloud, and visualized through interactive dashboards created with Streamlit and Tableau.

## Visual Representations

### Streamlit App Interface
![Screenshot 2024-08-22 at 18 37 16](https://github.com/user-attachments/assets/fd43e89f-5a35-4152-b1ff-c49999212842)

The Streamlit app provides a user-friendly interface for exploring and visualizing the Tokyo 2021 Olympics data. Users can select different tables and view visualizations directly within the app.

### Streamlit Visualization

![Screenshot 2024-08-22 at 18 37 32](https://github.com/user-attachments/assets/e43f51e4-8f36-443c-ac75-eb28c535e708)

An example of a data visualization created within the Streamlit app, showing the number of coaches by country in the basketball event.
## Integration with LangChain and OpenAI

This project also integrates with LangChain and OpenAI to enhance the analysis and provide a conversational interface for querying the Olympic data.

### How to Use LangChain and OpenAI for Querying

Iuse LangChain to create a seamless connection between our data and OpenAI's powerful language models. This allows users to ask natural language questions about the Olympic data and receive detailed answers.

To set this up, follow these steps:

1. **Install the necessary libraries:**

   ```
   pip install langchain openai
   ```

2. **Set up your OpenAI API key:**

   Make sure to store your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```

4. **Ask Questions:**

   Now you can ask questions like:

   - "Which country won the most medals in the Tokyo 2021 Olympics?"
   - "What is the correlation between the number of athletes and medal count?"

This integration allows for a more interactive and user-friendly exploration of the Olympic data, making it easier to derive insights and answers from the dataset.
### Olympic Chatbot Response

![image](https://github.com/user-attachments/assets/cebf55b0-2432-449b-83ad-d901faed1ef9)

The Olympic Chatbot, powered by LangChain and OpenAI, provides answers to natural language questions based on the Olympics data. In this example, the chatbot answers a query about the country with the most athletes participating in the Tokyo 2021 Olympics.

### LLM to SQL Flow

![Screenshot 2024-08-16 at 15 46 11](https://github.com/user-attachments/assets/49bb756f-502f-473b-ad61-5d89f5edc29e)

This image illustrates how a Large Language Model (LLM) can be used to transform a natural language question into a SQL query, retrieve the data from a SQL database, and then provide an answer back to the user.
## Data Sources

- [2021 Olympics in Tokyo Dataset](#https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo/data)
