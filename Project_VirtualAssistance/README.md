# Desktop Assistant - Jarvis

This is a simple desktop assistant named Jarvis, created using Python. Jarvis can perform various tasks such as opening YouTube and Google, telling the current day and time, and opening Notepad and Calculator. The assistant responds to voice commands and interacts with the user through speech.

## Features
- **Open YouTube**: Voice command to open YouTube in the default web browser.
- **Open Google**: Voice command to open Google in the default web browser.
- **Tell the Day**: Jarvis can tell you the current day of the week.
- **Tell the Time**: Jarvis can tell you the current time.
- **Open Notepad**: Voice command to open the Notepad application.
- **Open Calculator**: Voice command to open the Calculator application.
- **Search YouTube**: Perform a YouTube search based on voice input.
- **Greeting and Introduction**: Jarvis greets you and introduces itself.

## Prerequisites
- Python 3.x
- `pyttsx3` library
- `SpeechRecognition` library
- `pyaudio` library
- `webbrowser` module
- `datetime` module
- `os` module

## Installation
1. **Install Python**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Use `pip` to install the required libraries:
    ```sh
    pip install pyttsx3 SpeechRecognition pyaudio
    ```

## Usage
1. **Run the Script**: Execute the Python script to start the desktop assistant.
    ```sh
    python jarvis.py
    ```

2. **Give Commands**: Speak to Jarvis using the following commands:
    - "Open YouTube"
    - "Open Google"
    - "Which day it is"
    - "Tell me the time"
    - "Open Notepad"
    - "Open Calculator"
    - "Search YouTube [your query]"

3. **Terminate**: Say "Bye" to end the session with Jarvis.

## Code Explanation
Here's a brief explanation of the main functions in the code:
- `takeCommand()`: Listens to the user's voice and converts it into text.
- `speak(audio)`: Converts text to speech and communicates with the user.
- `tellDay()`: Informs the user about the current day of the week.
- `tellTime()`: Informs the user about the current time.
- `Hello()`: Greets the user.
- `searchYouTube(query)`: Searches YouTube based on the user's query.
- `openApplication(appName)`: Opens specified applications like Notepad and Calculator.
- `Take_query()`: Main function to handle user queries and execute corresponding commands.

## Contributing
Feel free to fork this repository and make modifications to enhance the functionality of Jarvis. Pull requests are welcome!

## License
This project is licensed under the MIT License.

## Acknowledgements
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyaudio](https://pypi.org/project/PyAudio/)

---

Happy coding!
