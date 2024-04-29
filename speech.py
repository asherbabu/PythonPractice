import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha

def search(query):
    try:
        id_app = "PPQAUL-X6JT2E9G8K"
        client_app = wolframalpha.Client(id_app)
        a = client_app.query(query)
        answer = next(a.results).text
        print(answer)
        text_speak("The answer for your question is: " + answer)
    
    except Exception as e:
        print(e)
        query_split = query.split(' ')
        query = " ".join(query_split[0:])
        text_speak("I am searching for " + query)
        print(wikipedia.summary(query, sentences=2))
        text_speak(wikipedia.summary(query, sentences=2))

def text_speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

query = input("Enter your query: ")
query = query.lower()

if query == '':
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source, 5)
        audio = r.listen(source)
        
    try:
        speech = r.recognize_google(audio)
        search(speech)
    
    except sr.UnknownValueError:
        print("Your speech is not understood by the Google Speech Recognition.")
    
    except sr.RequestError as e:
        print("Google Speech Recognition is not able to request the results for you: {0}".format(e))

else:
    search(query)