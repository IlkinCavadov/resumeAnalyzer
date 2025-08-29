from text_normalyzer import normalize_text
from similarity import similarity_score
from PyPDF2 import PdfReader
import streamlit as st
import plotly.graph_objects as go

st.title("Resume Analyzer")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description here")
if uploaded_file and job_description:
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    resume_clean = normalize_text(resume_text)
    description_clean = normalize_text(job_description)
    score = similarity_score(resume_clean, description_clean)

    st.subheader(f"Resume Fit Score: {score} / 100")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Resume Fit Score"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 30], 'color': 'red'},
                   {'range': [30, 50], 'color': 'yellow'},
                   {'range': [50, 70], 'color': 'lightgreen'},
                   {'range': [70, 100], 'color': 'green'}]}))

    st.plotly_chart(fig)
#print(f"Match Score : {score}")



