import speech_recognition as sr
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import os

app = FastAPI()
r = sr.Recognizer()

class Audio(BaseModel):
    audio: str

@app.post("/api/stt")
def process_audio(audio: Audio):
    audio_wav = base64.b64decode(audio.audio)
    
    wav_file = open("temp.wav", "wb")
    wav_file.write(audio_wav)

    with sr.AudioFile('temp.wav') as source:
        try:
            audio_text = r.listen(source)    
            text = r.recognize_google(audio_text,language = "en-IN")
            #print(text)
            return {"text":text}
        except:
            return {"err": "something went wrong"}