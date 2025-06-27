import speech_recognition as sr
import tkinter as tk 
import chess



     

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer.listen(mic)

        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            texto = texto.lower()
            print(f"{texto}")
        except sr.UnknownValueError as erro:
            print("Não entendi o que você disse")
            recognizer
            continue 
