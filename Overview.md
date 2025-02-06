***Ouline***
A virtual desktop assistant is truly impressive. Imagine your computer responding to your commands just like Jarvis did for Tony Stark! With Python, this is entirely possible. Python provides a robust library, enabling the creation of a virtual assistant. On Windows, you can utilize Sapi5, while Linux users can turn to Espeak for voice capabilities. Although this represents a basic form of artificial intelligence, it opens the door to endless possibilities.

***Modules needed***
pyttsx3
SpeechRecognition
webbrowser

pip install pyttsx3
pip install SpeechRecognition
pip install webbrowser

***Methods used for Virtual Assistant**
1) Speak Method
    Speak Method will help us in taking the voice from the machine. Here is the code explanation of Speak Method
2) Take query method
    This method will check for the condition. If the condition is true it will return output. We can add any number if conditions for it and if the condition satisfy we will get the desired output
3)  takeCommand  method
     This method is for taking the commands and recognizing the command from the speech_Recognition module
4) tellTime method
    This method will take time and slice it "2020-06-05 17:50:14.582630" from 11 to 12 for hour and 14-15 for min and then speak function will be called and then it will speak the current time
5) Hello method       
    This is just used to greet the user with a hello message
6) Main method
    Main method is the method where all the files get executed so we will call the Take_query method here so that it can recognize and tell or give us the desired output.     


Open YouTube and Google

Tell the current day and time

Open Notepad and Calculator

Perform YouTube searches

Respond with its name and greet you
