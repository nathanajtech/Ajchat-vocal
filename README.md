# Ajchat Vocal
<p align="center">
  <img src="images/ajchat_logo.png" alt="Ajchat Vocal Logo" width="200"/>
</p>

**Ajchat Vocal** se yon asistan vwa an kreyòl ki ka koute sa w di epi reponn ou ak vwa.

## Fonksyonalite

- Koute kòmand ou an kreyòl (ex: "Bonjou", "Ki lè li ye", "Orevwa")
- Reponn ak vwa pa li
- Entèfas modèn ak bouton pou kòmanse koute
- Aksyon fèt an tan reyèl ak repons vizyèl sou fenèt la

## Teknoloji itilize

- Python
- `SpeechRecognition` — pou rekonesans vwa
- `pyttsx3` — pou pale ak ou
- `customtkinter` — pou entèfas bèl ak modèn
- `pipwin` — pou enstale `pyaudio` fasil sou Windows

## Enstalasyon

```bash
git clone https://github.com/nathanajtech/Ajchat-vocal.git
cd Ajchat-vocal
pip install -r requirements.txt
pipwin install pyaudio
python ajchat_vocal.py
