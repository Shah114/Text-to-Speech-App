# Importing Modules
import streamlit as st
from gtts import gTTS
import tempfile
import os

# Function to generate and play TTS
def do_tts(text):
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(temp_file.name)
    temp_file.close()
    
    # Read the MP3 file content as binary to enable downloading
    with open(temp_file.name, "rb") as f:
        mp3_data = f.read()
    
    return temp_file.name, mp3_data

# Streamlit interface
st.title("Text to Speech💬")

# Text input from user
text_input = st.text_input("Enter text to convert to speech:")

# Button to generate and play TTS
if st.button("Convert to Speech"):
    if text_input:
        file_path, mp3_data = do_tts(text_input)
        
        # Play audio in Streamlit
        with open(file_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        
        # Offer download of the MP3 file
        st.download_button(label="Download MP3", data=mp3_data, file_name="speech.mp3", mime="audio/mp3")
        
        # Now that the file is closed, delete it
        os.remove(file_path)
    else:
        st.write("Please enter some text.")