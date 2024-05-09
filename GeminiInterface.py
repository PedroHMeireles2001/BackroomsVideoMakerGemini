from gtts import gTTS
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name='gemini-1.0-pro')
def sanitize(markdown):
    response = model.generate_content("turn this markdown into user-friendly, markdown-free text:"+markdown)
    return response.text

def scripting(text):
    response = model.generate_content(f"Separate the following text into the specified parts:\nText: ```{text}````\n Separate the text into the following parts:\n1. Name\n2. Difficulty Class\n3. Detailed Description\n4. Entrances and Exits\n5. Entities\n6. Bases ")
    script = response.text
    script = script.replace("- ", "")
    script = script.replace("1. ", "")
    script = script.replace("2. ", "")
    script = script.replace("3. ", "")
    script = script.replace("4. ", "")
    script = script.replace("5. ", "")
    script = script.replace("6. ", "")
    script = script.replace("*","")
    return script


def make_audio(text,file,language="en-US"):
    tts = gTTS(text=text, lang=language)
    tts.save(f"{file}.mp3")
