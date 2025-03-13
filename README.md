# Voice Assistant (Jarvis) 🗣️

This is a simple voice assistant built using Python. The assistant listens to voice commands, processes them, and performs various tasks like retrieving information from Wikipedia, opening applications, searching Google, and more.

## 🔥 Features
- 🎤 **Speech Recognition** - Listens to voice commands using `speech_recognition`.
- 🔊 **Text-to-Speech (TTS)** - Uses `pyttsx3` to respond with a human-like voice.
- 🕒 **Get Time & Date** - Fetches the current time and date.
- 📖 **Wikipedia Search** - Retrieves brief Wikipedia summaries.
- 🌐 **Google Search** - Searches queries on Google.
- 📝 **Open Applications** - Opens Notepad and Calculator.
- 🛑 **Exit Command** - Can stop execution upon request.

## 🛠️ Requirements
Ensure you have the following dependencies installed before running the project:

```sh
pip install speechrecognition pyttsx3 wikipedia
```

Additionally, you may need to install `pyaudio`:
- **Windows:**  
  ```sh
  pip install pyaudio
  ```
- **Linux:**  
  ```sh
  sudo apt-get install portaudio19-dev && pip install pyaudio
  ```

## 🚀 How to Run
1. Clone this repository or copy the script into a Python file.
2. Run the script:
   ```sh
   python assistant.py
   ```
3. Speak commands prefixed with `"Jarvis"`, such as:
   - `"Jarvis, what is the time?"`
   - `"Jarvis, search Wikipedia for Python programming."`
   - `"Jarvis, open Notepad."`
   - `"Jarvis, search Google."`

## 🎯 Supported Commands
| Command | Function |
|---------|----------|
| `"hello"` | Greets the user |
| `"time"` | Tells the current time |
| `"date"` | Tells today's date |
| `"wikipedia [query]"` | Searches Wikipedia and reads a summary |
| `"open notepad"` | Opens Notepad |
| `"open calculator"` | Opens Calculator |
| `"search google"` | Prompts user for a query and searches Google |
| `"exit"` or `"stop"` | Stops the assistant |

## 📝 Future Improvements
- Add more application launchers.
- Implement wake word detection (e.g., "Hey Jarvis" without requiring manual invocation).
- Add integration for music playback and weather updates.

## 💡 Contributing
Feel free to fork this repository and make improvements! If you have suggestions, open an issue or submit a pull request.

## 🏆 Author
**MD ZUBAIRUDDIN**  
📧 Contact: zubair.uddin005@gmail.com

---

Enjoy using your personal voice assistant! 🎙️🤖
```

This `README.md` includes:
- **Project Overview**
- **Features**
- **Installation Instructions**
- **Usage Guide**
- **Supported Commands**
- **Future Enhancements**
- **Author Information**
