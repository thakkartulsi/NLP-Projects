# ---Imports---

import speech_recognition as sr
import pyttsx3
from langdetect import detect
from gtts import gTTS
import os

# Function for Language Detection
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'en' # Default to English if detection fails
    
# Function for Speech-to-Text Conversion
def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Say something...')
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print('You said: ', text)
        return text
    except sr.UnknownValueError:
            print('Could not understand audio')
            return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return ""
    
# Function for Text-to-Speech Conversion

def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save("translated_speech.mp3")
        os.system("start translated_speech.mp3")
    except Exception as e:
        print(f"Error in Text-to-Speech: {e}")
