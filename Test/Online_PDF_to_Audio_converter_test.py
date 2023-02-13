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
