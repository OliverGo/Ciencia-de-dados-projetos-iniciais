import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        audio = recognizer.listen(mic)
        texto = recognizer.recognize_google(audio, language='pt-BR')
        texto = texto.lower()
        print(f"{texto}")