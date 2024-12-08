from gtts import gTTS
import os

x = open("text_to_speech.txt")
y = x.read()

language = 'en'

audio = gTTS(text=y, slow=True)

audio.save("audio.wav")
os.system("audio.wav")