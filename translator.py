import speech_recognition as sr
from googletrans import Translator, constants
import pyttsx3

# Defining the voices so it can talk
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Parameters
fr = voices[3].id 
en = voices[2].id
es = voices[0].id
it = voices[4].id

language = "fr"
voices = fr

r = sr.Recognizer()
translator = Translator()


engine.setProperty('rate', 170)
engine.setProperty('voice', voices)
engine.setProperty('volume', 20)

# speak function will pronounce the string is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Talk...")
    audio_text = r.listen(source)

    try:
        print("Text: "+r.recognize_google(audio_text, language="es"))
        store_text = r.recognize_google(audio_text, language="es")

        print("Translating...")
        
        # Translate the giving text
        translation = translator.translate(str(store_text), dest=language)
        print(translation.text)

        speak(translation.text)
    except:
        print("Sorry, I did not get that")
