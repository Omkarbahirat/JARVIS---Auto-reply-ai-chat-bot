import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # Try [1] for female voice
engine.setProperty('rate', 180)             # Speed of speech
engine.say("Yes, I'm listening.")
engine.runAndWait()
