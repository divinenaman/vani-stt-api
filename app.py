import speech_recognition as sr
import base64
from flask import Flask
from flask import request, jsonify
import os

app = Flask(__name__)
r = sr.Recognizer()


@app.route("/api/stt",methods=["POST"])
def hello_world():
    body = request.get_json()
    audio_base64 = body.get('audio')
    audio_wav = base64.b64decode(audio_base64)
    
    wav_file = open("temp.wav", "wb")
    wav_file.write(audio_wav)

    with sr.AudioFile('temp.wav') as source:
        try:
            audio_text = r.listen(source)    
            text = r.recognize_google(audio_text,language = "en-IN")
            #print(text)
            return jsonify({"text":text})
        except:
            return jsonify({"err": "something went wrong"})

port = int(os.environ.get('PORT', 5000))                
app.run(debug=True,port=port)    