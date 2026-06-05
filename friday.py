import tkinter as tk
import math
import time
import webbrowser
import subprocess

from speech_whisper import take_command
from chatbot import chatbot_answer

# ---------------- STABLE WINDOWS TTS ----------------
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

# ---------------- FRIDAY GUI ----------------
class FridayGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FRIDAY AI Assistant")
        self.root.geometry("520x620")
        self.root.configure(bg="#0f0f0f")

        self.state = "IDLE"

        self.canvas = tk.Canvas(root, width=300, height=300,
                                bg="#0f0f0f", highlightthickness=0)
        self.canvas.pack(pady=20)

        self.circle = self.canvas.create_oval(
            120, 120, 180, 180, fill="#1f6fff", outline=""
        )

        self.text = tk.Text(
            root, height=12, width=55,
            bg="#111", fg="white",
            wrap="word", font=("Consolas", 10)
        )
        self.text.pack(pady=10)
        self.text.insert(tk.END, "🤖 Friday is online.\n\n")
        self.text.configure(state="disabled")

        self.angle = 0
        self.animate()

        self.root.after(1000, self.main_loop)

    def add_text(self, msg):
        self.text.configure(state="normal")
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)
        self.text.configure(state="disabled")

    def animate(self):
        r = 30
        if self.state == "LISTENING":
            r = 38 + 6 * math.sin(self.angle)
        elif self.state == "THINKING":
            r = 35 + 12 * math.sin(self.angle * 2)
        elif self.state == "SPEAKING":
            r = 45 + 10 * math.sin(self.angle * 3)

        self.canvas.coords(self.circle, 150-r, 150-r, 150+r, 150+r)
        self.angle += 0.08
        self.root.after(30, self.animate)

    def main_loop(self):
        self.state = "SPEAKING"
        speak("Hello Shiv. I am Friday.")
        self.add_text("🤖 Friday: Hello Shiv.\n")

        while True:
            self.state = "LISTENING"
            self.add_text("🎙️ Listening...")
            self.root.update()

            query = take_command()
            if not query:
                continue

            self.add_text(f"🧑 Shiv: {query}")

            if "exit" in query or "bye" in query:
                self.state = "SPEAKING"
                speak("Goodbye Shiv")
                self.add_text("🤖 Friday: Goodbye Shiv")
                break

            if "open youtube" in query:
                self.state = "SPEAKING"
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")
                continue
            if "open google" in query:
                self.state = "SPEAKING"
                speak("Opening Google")
                webbrowser.open("https://google.com")
                continue
            if "open spotify" in query:
                self.state = "SPEAKING"
                speak("Opening Spotify")
                webbrowser.open("https://spotify.com")
                continue

            self.state = "THINKING"
            self.add_text("🤖 Friday is thinking...")
            self.root.update()

            answer = chatbot_answer(query)

            self.state = "SPEAKING"
            speak(answer)
            self.add_text(f"🤖 Friday: {answer}\n")

            self.state = "IDLE"

# ---------------- RUN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FridayGUI(root)
    root.mainloop()
