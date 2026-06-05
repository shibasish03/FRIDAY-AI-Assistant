import whisper
import sounddevice as sd
import scipy.io.wavfile as wav

model = whisper.load_model("base")

def take_command():
    fs = 44100
    duration = 5

    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write("input.wav", fs, recording)

    result = model.transcribe("input.wav")
    return result["text"].lower()
