from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_answer
from speech_whisper import take_command
import subprocess

app = Flask(__name__)

# ----------- TTS -----------
def speak(text):
    safe_text = text.replace('"', "'")
    command = f'''
    Add-Type -AssemblyName System.Speech;
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;
    $speak.Speak("{safe_text}");
    '''
    subprocess.run(
        ["powershell", "-Command", command],
        creationflags=subprocess.CREATE_NO_WINDOW
    )

# ----------- ROUTES -----------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/listen")
def listen():
    query = take_command()
    return jsonify({"query": query})

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    query = data.get("query", "")

    if "open youtube" in query:
        subprocess.Popen(["start", "https://youtube.com"], shell=True)
        return jsonify({"response": "Opening YouTube"})

    if "open google" in query:
        subprocess.Popen(["start", "https://google.com"], shell=True)
        return jsonify({"response": "Opening Google"})

    if "open spotify" in query:
        subprocess.Popen(["start", "https://spotify.com"], shell=True)
        return jsonify({"response": "Opening Spotify"})

    answer = chatbot_answer(query)
    speak(answer)

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)