import speech_recognition as sr
import pyttsx3
import datetime

def pale(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def koute():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Koute...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="ht-HT")
        print(f"Ou di: {command}")
        return command.lower()
    except sr.UnknownValueError:
        pale("Mwen pa tande byen. Tanpri repete.")
        return ""
    except sr.RequestError:
        pale("Sistèm rekonesans vwa a pa disponib.")
        return ""

def reponn(command):
    if "bonjou" in command:
        pale("Bonjou! Kijan ou ye?")
    elif "ki lè li ye" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        pale(f"Kounye a li {now}")
    elif "au revoir" in command or "orevwa" in command:
        pale("Oke, n a wè pita!")
        exit()
    else:
        pale("Mwen pa konprann sa ou di a.")

if __name__ == "__main__":
    pale("Ajchat Vocal pare pou sèvi ou.")
    while True:
        cmd = koute()
        if cmd:
            reponn(cmd)
