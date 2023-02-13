import os
import re
import sys
import io
import PyPDF2
from gtts import gTTS
import streamlit as st
from googletrans import Translator, LANGUAGES
import pytest

def test_translate_and_save_audio():
    string_words = "Hello World"
    dest_language = "fr"
    expected_result = "Bonjour le monde"

    translator = Translator()
    result = translator.translate(string_words, dest=dest_language)
    assert result.text == expected_result

    audio = gTTS(text=result.text, lang=dest_language)
    audio_file = 'test.mp3'
    audio.save(audio_file)
    assert os.path.exists(audio_file)

    os.remove(audio_file)
    assert not os.path.exists(audio_file)

def test_pdf_to_audio_converter():
    pdf_data = io.BytesIO(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj\n<</Type/Catalog/Pages 2 0 R>>\nendobj\n2 0 obj\n<</Type/Pages/Kids[3 0 R]/Count 1>>\nendobj\n3 0 obj\n<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]>>\nendobj\nxref\n0 4\n0000000000 65535 f \n0000000018 00000 n \n0000000077 00000 n \n0000000139 00000 n \ntrailer\n<</Size 4/Root 1 0 R>>\nstartxref\n194\n%%EOF\n')
    dest_language = "fr"
    expected_result = ""

    pdf_file = io.BytesIO(pdf_data.read())
    pdffile = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = pdffile.getNumPages()

    string_words = ''
    for pages in range(no_of_pages):
        pi = pdffile.getPage(pages)
        page = pdffile.getPage(pages)
        content = page.extractText()
        textonly = re.findall(r'[a-zA-Z0-9]+', content)
        string_words =  " ".join(textonly)
        print(string_words)

    from googletrans import LANGUAGES
    language_names =  {
        "Afrikaans": "af",
        "Albanian": "sq",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Portuguese": "pt",
        "Mandarin": "zh-CN"
    }
    language = "French"
    lang_code_map = {
        "Afrikaans": "af",
        "Albanian": "sq",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Portuguese": "pt",
        "Mandarin": "zh-CN"
    }

    translator = Translator()
    translator.detect(string_words)
    result = translator.translate(string_words, dest=language)
    
    lang_code = lang_code_map.get(language, "en")  # default to "en" if language not found

    audio = gTTS(text=result.text, lang=lang_code)
    audio_file = 'listen_6_pdf.mp3'
    audio.save(audio_file)
    assert os.path.exists(audio_file) == True
    
    # Cleanup audio file
    os.remove(audio_file)