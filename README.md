# JARVIS---Auto-reply-ai-chat-bot
JARVIS is a simple voice-activated assistant built with Python. It uses speech recognition to detect the wake word “Jarvis” and text-to-speech (TTS) to respond with a human-like voice. Once activated, JARVIS can execute spoken commands such as opening websites or performing basic tasks.

🚀 Features

🎙️ Wake Word Detection: Activates on “Jarvis”.

🗣️ Voice Feedback: Responds with natural speech (via pyttsx3).

🌐 Web Control: Can open Google, YouTube, and other sites.

🧩 Custom Commands: Easily expandable to add more functions.

💻 Offline TTS: Works without an internet connection for speech output.

🧰 Technologies Used
Component	Purpose
SpeechRecognition	Converts your voice to text
pyttsx3	Text-to-speech engine for voice output
pyaudio	Captures microphone input
webbrowser	Opens websites via spoken commands
time	Adds timing and pauses for smooth flow
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/jarvis-voice-assistant.git
cd jarvis-voice-assistant

2️⃣ Install dependencies

Make sure Python 3.10+ is installed.
Then run:

pip install pyttsx3 SpeechRecognition pyaudio


💡 If pyaudio fails to install, use:
pip install pipwin → pipwin install pyaudio

▶️ Usage

Run the assistant:

python jarvis.py


Then say:

“Jarvis” → activates the assistant

“open Google” → opens Google in your browser

“open YouTube” → opens YouTube

“stop” → exits the program

Example Output:
Say 'Jarvis' to activate me...
You said: jarvis
JARVIS: Yes, I'm listening.
Activated. Listening for your command...
You said: open google
JARVIS: Opening Google.

🧩 Add Your Own Commands

You can easily add more features:

elif "open github" in command:
    speak("Opening GitHub.")
    wb.open("https://github.com")


Add as many custom voice commands as you like.

🧠 How It Works

The assistant continuously listens for the word “Jarvis.”

Once detected, it responds “Yes, I’m listening.” via the text-to-speech engine.

It then listens for the next voice command, converts it to text, and performs the corresponding action.

🪄 Future Enhancements

Integrate ChatGPT API for conversational abilities.

Add desktop control (open apps, play music).

Include weather, time, and news updates.

Create a GUI interface for visual feedback.

🧑‍💻 Author

Omkar Bahirat
🎓 MIT ADT University
💡 Developed for a Python voice assistant project demonstration
