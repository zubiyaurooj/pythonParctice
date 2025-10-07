import speech_recognition as sr
import datetime
import webbrowser
import os
from gtts import gTTS
from playsound import playsound
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito") 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver.get("https://www.youtube.com/")

# ------------------- SPEAK FUNCTION USING gTTS -------------------
def speak(text):
    print("Jarvis:", text)
    temp_file = "temp_voice.mp3"   # Save in current folder to avoid permission issues
    tts = gTTS(text=text, lang='en')
    tts.save(temp_file)
    playsound(temp_file)
    os.remove(temp_file)

# ------------------- SPEECH RECOGNITION -------------------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except:
        print("Sorry, I didn’t catch that.")
        return "none"
    return query.lower()

# ------------------- GREETING -------------------
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis, your personal assistant. How can I help you?")

# ------------------- MAIN PROGRAM -------------------
if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
            time.sleep(2)

            driver.find_element("xpath",'//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]').send_keys("python in one")
            time.sleep(2)
            driver.find_element("xpath",'//button[@class="ytSearchboxComponentSearchButton"]').click


        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\Public\\Music"  # change path if needed
            try:
                songs = os.listdir(music_dir)
                if songs:
                    speak("Playing music")
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in your music folder.")
            except:
                speak("Music folder not found. Please check the path.")

        # --- Conversation Replies ---
        elif "who are you" in query or "who r u" in query:
            speak("I am Jarvis, your personal assistant, created to make your life easier.")

        elif "how are you" in query or "how r u" in query:
            speak("I am always fine when I am helping you, Sir.")

        elif "hello" in query or "hi jarvis" in query:
            speak("Hello Sir, nice to hear from you.")

        elif "thank you" in query:
            speak("You're welcome Sir!")

        elif "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye Sir, have a nice day!")
            break
