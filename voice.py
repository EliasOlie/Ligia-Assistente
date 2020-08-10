import pyttsx3
import random

speak = pyttsx3.init('sapi5')

error_logs = ['Desculpe, não entendi', 'Repita, por gentiliza', 'Não consegui entender, repita mais devagar']

while True:
    prhase = random.choice(error_logs)
    speak.say(prhase)
    speak.runAndWait()