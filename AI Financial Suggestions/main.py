import streamlit as st
from dotenv import load_dotenv
import io
import os
import google.generativeai as genai
import pandas as pd

load_dotenv()

st.title("AI Financial Analyser")
st.badge("Make better Financial Decision with AI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your financial data as csv", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    tab1, tab2, tab3 = st.tabs(["Raw Data", "Cleaned Data" ,"AI Insights"])

    with tab1:
        st.subheader('Raw Data')
        st.dataframe(df)

    with tab2:
        st.subheader("Cleaned Data")
        df['Amount'] = pd.to_numeric(df['Amount'], errors="coerce")

    with tab3:
        st.subheader("Using AI Analysis")
        prompt = f"""  
                Analyze the following financial data provided in CSV format.
                The data includes columns for 'Date' , 'Category','Descrption', 'Amount' and 'Payment Method'.
                Provide insights based on this data, including:
                1. A summary of total income and expenses.
                2. A breakdown of expenses by category.
                3. Identification of the most frequently used payment methods.
                4. Any other interesting observations or pattern you can find in the data.



                Here is the data : {df.to_csv(index=False)}
                           """

        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            response = model.generate_content(prompt)
            st.markdown('#### AI Suggestions ')
            st.write(response.text)
        except Exception as e:
            st.error(f"Exception Ocurred {e}")

