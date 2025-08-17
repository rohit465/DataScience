import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai

load_dotenv()

st.title("Rohit Nimangre")
st.badge("Chai Code")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your Resume here (PDF or Txt only)", type=["pdf", "txt"])
job_role = st.text_input("Enter your Job Role here that you are targeting.")

analyze = st.button("Analyze Resume")
print(analyze)

def extract_text_from_pdf(file_bytes):
    print('for extract from pdf')
    reader = PyPDF2.PdfReader(file_bytes)
    print('reaing bytes')
    return "\n".join(page.extract_text() or "" for page in reader.pages)




def extract_text(uploaded_file):
    print("inside extract text()")
    file_type = uploaded_file.type
    print('file type is ', file_type)
    if file_type == "application/pdf":
        print('for pdf')
        with io.BytesIO(uploaded_file.read()) as file_bytes:
            return extract_text_from_pdf(file_bytes)
    elif file_type == "text/plain":
        print('for txt')
        return uploaded_file.read().decode("utf-8")


if analyze and uploaded_file:
    try:
        print("**********   ",uploaded_file)
        file_content = extract_text(uploaded_file)
        print("---------   ",file_content)
        if not file_content.strip():
            st.error("File Doesn't have any content.")
            st.stop()

        #AI Calling

        prompt = f"""
                    You are brutally honest, no non-sense HR expert who's been reviewing resumes for decades
                    Roast this resume like you are on a comedy stage but still give some usefull insights feedback
                    Don't hold back - be sarcastic, witty and critically where needed.
                    Would make this resume actually land a job in {job_role}  for a company.

                    here is the resume go wild:
                    {file_content}
                    Make it sting and make sure to keep it in 150-200 words. 

                    """
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.markdown("    Analysis Result    ")
        st.markdown(response.text)



    except Exception as e:
        st.error(f"Exception Occured. {e}")