# ---Imports---
import streamlit as st
from utils import detect_language, text_to_speech, speech_to_text
from model import build_model
from googletrans import Translator

# ---Set Page Title and Favicon---
st.set_page_config(
    page_title="TransLang",  # Title of the page
    page_icon="https://img.icons8.com/color/96/translation.png",  # Favicon URL
)

# ---Translation Function---
def translate(text, src_lang, tgt_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=tgt_lang)
    return translation.text

# ---Streamlit User Interface---
st.markdown("<h1 style='text-align: center;'>TransLang: A Multilingual Translator</h1>", unsafe_allow_html=True)

# Add icons or images
st.markdown("""
    <div style="text-align: center;">
        <img src="https://img.icons8.com/color/96/translation.png" alt="Translation Icon">
    </div>
""", unsafe_allow_html=True)

input_text = st.text_area('Enter text to translate:')

# ---List of Supported Languages---
languages = {
    'ar': 'Arabic',
    'zh-cn': 'Chinese',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'fi': 'Finnish',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'es': 'Spanish',
    'sv': 'Swedish',
    'th': 'Thai',
    'tr': 'Turkish',
    'vi': 'Vietnamese'
}

# ---Dropdowns for Language Selection---
src_lang_display = st.selectbox('Select Source Language', [f"{code} - {name}" for code, name in languages.items()])
tgt_lang_display = st.selectbox('Select Target Language', [f"{code} - {name}" for code, name in languages.items()])

# Extract language codes from dropdown values
src_lang = src_lang_display.split(' - ')[0]
tgt_lang = tgt_lang_display.split(' - ')[0]

# ---Buttons in a Single Line---
col1, col2, col3 = st.columns(3)

with col1:
    detect_button = st.button('🔍 Detect Language')
with col2:
    translate_button = st.button('🔄 Translate')
with col3:
    speak_button = st.button('🎤 Speak to Translate')

# ---Outputs---
if detect_button:
    if input_text.strip():
        detected_language = detect_language(input_text)
        st.write(f'Detected language: {detected_language}')
    else:
        st.error("Please enter some text for language detection.")

if translate_button:
    if input_text.strip():
        try:
            translated_text = translate(input_text, src_lang, tgt_lang)
            st.write("Translated Text:")
            st.write(translated_text)
        except ValueError as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter text to translate.")

if speak_button:
    speech_text = speech_to_text()
    if speech_text:
        st.write(f"Speech Input: {speech_text}")
        try:
            translate_speech = translate(speech_text, src_lang, tgt_lang)
            st.write(f"Translated Speech: {translate_speech}")
            text_to_speech(translate_speech)
        except ValueError as e:
            st.error(f"Error during translation: {e}")
    else:
        st.error("No speech input detected. Please try again.")











