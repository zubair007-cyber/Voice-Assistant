import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
# Initialize the voice engine

engine = pyttsx3.init()
def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()
ASSISTANT_NAME = "jarvis"  # You can rename it to anything
def listen():
    """Captures user's voice input and converts it into text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture the user's speech

        try:
            command = recognizer.recognize_google(audio).lower()  # Convert speech to text
            print(f"🗣 You said: {command}")

            if ASSISTANT_NAME in command:  # Check if the assistant's name is mentioned
                return command.replace(ASSISTANT_NAME, "").strip()  # Remove the name and return the actual command
            else:
                return None  # Ignore if the name is not called

        except sr.UnknownValueError:
            print("❌ Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("❌ Network error.")
            return None


def respond(command):
    """Processes user commands and performs tasks."""
    if "hello" in command:
        speak("Hello! How can I assist you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}")


    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "open notepad" in command:
        speak("Opening Notepad...")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator...")
        os.system("calc")

    elif "search google" in command:
        speak("What should I search for?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching Google for {search_query}")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# Run the assistant
if __name__ == "__main__":
    speak(f"Hello! I am {ASSISTANT_NAME}. How can I help you?")
    
    while True:
        command = listen()
        if command:  # Only process the command if the assistant's name was mentioned
            respond(command)

