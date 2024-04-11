import streamlit as st

def text_to_speech(text):
    tts = gtts.gTTS(text=text, lang='en')
    sound_file = BytesIO()
    tts.write_to_fp(sound_file)
    sound_file.seek(0)
    st.audio(sound_file, format='audio/mp3')

text_to_speech('Hello, Streamlit!')
