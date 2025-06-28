import speech_recognition as sr # Biblioteca para reconhecimeto de voz
import chess # Biblioteca para manipulação de xadrez
import re # Biblioteca para expressões regulares 

board = chess.Board()
print(board)
print(board.legal_moves)
     
def movimento(origem, destino):
    try:
        print(f"Esses são os movimentos validos: {board.legal_moves}")
        origem = chess.parse_square(origem)
        destino = chess.parse_square(destino)
        movimento = chess.Move(origem, destino)
        if movimento in board.legal_moves:
            board.push(movimento)
            print(board)
        else:
            print("movimento inválido")
    except ValueError as e:
        print(f"movimento irreconhecido (lista inválida)")    



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
origem = []
destino = []
def converte_comando(texto):

    texto = texto.lower()
    texto = normalizar_numeros(texto)
    texto = texto.replace(" ", "").replace("para", "").replace("é", "e")
    match = re.match(r"([a-h][1-8])([a-h][1-8])", texto)
    if match:
        origem.append(match.group(1))
        destino.append(match.group(2))
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
            movimento(origem, destino)
            print(origem, destino)
        except sr.UnknownValueError as erro:
            print("Não entendi o que você disse")
            recognizer
            continue