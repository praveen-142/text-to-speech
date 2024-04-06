import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech(text, lang='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)

    # Save the speech to BytesIO object
    speech_file = BytesIO()
    tts.write_to_fp(speech_file)

    return speech_file

def main():
    st.title("Text-to-Speech App")

    # Language selection
    lang = st.selectbox("Select language:", options=['en', 'fr', 'es', 'de'])

    # Text input
    text_input = st.text_area("Enter text to convert to speech:")

    if st.button("Convert to Speech"):
        if text_input:
            # Convert text to speech
            speech_file = text_to_speech(text_input, lang)
            st.audio(speech_file, format='audio/mp3', start_time=0)

if __name__ == "__main__":
    main()
