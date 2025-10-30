import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')  # use 'espeak' on Linux/macOS

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Network error.")
        return ""

if __name__ == "__main__":
    speak("Initializing JARVIS...")
    time.sleep(1)
    
    while True:
        print("\nSay 'Jarvis' to activate me...")
        wake_word = listen_command(timeout=3, phrase_time_limit=3)
        
        if "jarvis" in wake_word:
            speak("Yes, I'm listening.")
            time.sleep(0.5)
            print("Activated. Listening for your command...")
            
            command = listen_command()
            
            if "open google" in command:
                speak("Opening Google.")
                wb.open("https://www.google.com")
            
            elif "open youtube" in command:
                speak("Opening YouTube.")
                wb.open("https://www.youtube.com")
            
            elif "stop" in command or "exit" in command:
                speak("Goodbye! Shutting down.")
                break
            
            elif command.strip() == "":
                speak("I didn’t catch that. Please repeat.")
            
            else:
                speak("Sorry, I don’t know that command yet.")
