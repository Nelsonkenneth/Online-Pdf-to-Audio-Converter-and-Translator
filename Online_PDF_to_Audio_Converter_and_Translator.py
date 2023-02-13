import streamlit as st
import PyPDF2
from gtts import gTTS
from googletrans import Translator
import re
import os
from io import BytesIO

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "9 °C", "1 °C")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.title("PDF to Audio Converter")

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True, type=[".pdf",])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)

    pdf_file = BytesIO(bytes_data)
    pdffile = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = pdffile.getNumPages()

    string_words = ''
