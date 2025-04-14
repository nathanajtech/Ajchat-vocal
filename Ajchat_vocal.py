import customtkinter as ctk
import speech_recognition as sr
import pyttsx3
import datetime
import threading
from PIL import Image
import os

# Mete mòd aparans ak tèm
ctk.set_appearance_mode("Système")  # Oswa "Clair" ou "Sombre"
ctk.set_default_color_theme("blue")

# Kreye fenèt aplikasyon an
fichye_fenèt = ctk.CTk()
fichye_fenèt.title("Ajchat Vocal")
fichye_fenèt.geometry("500x300")

# Chaje logo a
image_path = os.path.join("images", "ajchat_logo.png")  # Asire logo a sou folder 'images'
logo_image = ctk.CTkImage(Image.open(image_path), size=(150, 150))

# Kreye etikèt pou logo a
logo_label = ctk.CTkLabel(fichye_fenèt, image=logo_image, text="")
logo_label.pack(pady=10)  # Ajoute logo anwo fenèt la

# Etikèt pou repons
etikèt_repons = ctk.CTkLabel(fichye_fenèt, text="Ajchat pare pou sèvi ou...", font=("Arial", 16))
etikèt_repons.pack(pady=20)

def pale(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def koute():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        etikèt_repons.configure(text="Koute...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="ht-HT")
        etikèt_repons.configure(text=f"Ou di: {command}")
        reponn(command.lower())
    except sr.UnknownValueError:
        pale("Mwen pa tande byen. Tanpri repete.")
        etikèt_repons.configure(text="Mwen pa tande byen.")
    except sr.RequestError:
        pale("Sistèm rekonesans vwa a pa disponib.")
        etikèt_repons.configure(text="Erè koneksyon ak sèvis vwa.")

def reponn(command):
    if "bonjou" in command:
        pale("Bonjou! Kijan ou ye?")
    elif "ki lè li ye" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        pale(f"Kounye a li {now}")
    elif "orevwa" in command:
        pale("Oke, n a wè pita!")
        etikèt_repons.configure(text="Fèmen aplikasyon an...")
        fichye_fenèt.after(2000, fichye_fenèt.destroy)
    else:
        pale("Mwen pa konprann sa ou di a.")
        etikèt_repons.configure(text="Mwen pa konprann sa...")

def koute_thread():
    t = threading.Thread(target=koute)
    t.start()

# Bouton pou koute vwa
bouton_koute = ctk.CTkButton(fichye_fenèt, text="Koute vwa mwen", command=koute_thread)
bouton_koute.pack(pady=20)

# Lanse aplikasyon an
fichye_fenèt.mainloop()
