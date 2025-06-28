import speech_recognition as sr
import tkinter as tk 
import chess
import re


     

recognizer = sr.Recognizer()

def normalizar_numeros(texto):
    numeros = {
        "um": "1", "dois": "2", "três": "3", "tres": "3",
        "quatro": "4", "cinco": "5", "seis": "6",
        "sete": "7", "oito": "8"
    }
    for palavra, numero in numeros.items():
        texto = texto.replace(palavra, numero)
    return texto


def converte_comando(texto):
    
    texto = texto.lower()
    texto = normalizar_numeros(texto)
    texto = texto.replace(" ", "").replace("para", "")
    match = re.match(r"([a-h][1-8])([a-h][1-8])", texto)
    if match:
         return match.group(1) + match.group(2)
    else:
        return "Numero/cassa irregular"

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer.listen(mic)

        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            texto = texto.lower()
            print(f"{converte_comando(texto)}")
        except sr.UnknownValueError as erro:
            print("Não entendi o que você disse")
            recognizer
            continue 
