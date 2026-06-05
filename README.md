readme life for the project
# FRIDAY – AI Voice Assistant

FRIDAY is a Python-based AI voice assistant inspired by intelligent virtual assistants from science fiction. It enables hands-free interaction through voice commands, natural language conversations, and voice responses, all within a desktop graphical interface.

The assistant listens to user input using speech recognition, processes requests using a Large Language Model (LLM), and responds through speech synthesis. In addition to answering questions, FRIDAY can perform basic actions such as opening websites and launching applications.

## Features

- Voice-controlled interaction
- Speech recognition using Whisper
- AI-powered conversations using Groq LLMs
- Voice responses using Windows Text-to-Speech
- Real-time graphical user interface
- Dynamic visual feedback for Listening, Thinking, and Speaking states
- Open websites and applications through voice commands
- Conversation history displayed within the interface

## Tech Stack

- Python
- Whisper
- Groq API
- Tkinter
- FFmpeg
- SoundDevice
- SciPy
- Windows Speech API

## Project Structure


FRIDAY-AI-Assistant/
│
├── chatbot.py
├── speech_whisper.py
├── friday.py
├── known_faces/
├── requirements.txt
├── README.md
└── screenshots/


## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/FRIDAY-AI-Assistant.git
cd FRIDAY-AI-Assistant
Create a virtual environment
python -m venv .venv
.venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Install FFmpeg and add it to your system PATH

Verify installation:

ffmpeg -version
Configure your Groq API key

Create a .env file:

GROQ_API_KEY=your_api_key_here
Run the application
python friday.py
Example Commands
"What is machine learning?"
"Open Google"
"Open YouTube"
"Open Spotify"
"Tell me a joke"
"Who is Alan Turing?"
Future Improvements
Wake-word detection ("Hey Friday")
Advanced desktop application control
Conversation memory
Enhanced UI and animations
Face authentication
Real-time audio visualizations
Disclaimer

This project was built for learning and experimentation purposes. It is not intended to be a production-ready virtual assistant.

Author

Shibasish Bhattacharjee

Computer Science Student | AI & Software Development Enthusiast.
