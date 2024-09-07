import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
import requests

# recognizer = sr.Recognizer()
ttsx = pyttsx3.init()
# ttsx.say("Hello Sir! Good Morning")
# ttsx.runAndWait()     
newsapi = "8efd82787aae45d58f36347037a4ba6f"

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processcommand(c):
    #Opening tasks-
    if "open google" in c.lower():
        speak(f"Opening {c.split(" ")[1]}")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak(f"Opening {c.split(" ")[1]}")
        webbrowser.open("https://youtube.com")

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=8efd82787aae45d58f36347037a4ba6f ")

    elif "how " in c.lower():
        speak("I am find sir, How are you ")


    # elif "play song" in c.lower():
    #     speak("Playing Song..")
    #     webbrowser.open("https://youtu.be/a3Ue-LN5B9U?si=U-jZQEM89_t_w19k&t=72")

    elif "test" in c.lower():
        print(c) 

    #Playing songs
    elif c.lower().startswith("play"):
        speak(f"playing the song...")
        song = c.lower().split(" ")[1]
        webbrowser.open(music_lib.music[song])
    else:
        speak("Please Try Again!")


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    #Listen for wake word for Jarvis
    while True:
        #obtain audio from the microphone
        r = sr.Recognizer()

        #Recognise the audio using Google
        try:
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            print("Recognizing....")
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Yes Sir! What you want me to do?")
                #Listen for command
                with sr.Microphone() as source:
                    print("Listning For A Command...")
                    audio = r.listen(source)
                print("Recognizing Command...")
                command = r.recognize_google(audio)
                print(command)
                processcommand(command)



            
       
        except Exception as e:
            (f"Error{e}")