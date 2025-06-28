import speech_recognition as sr # Biblioteca para reconhecimeto de voz
import chess # Biblioteca para manipulação de xadrez
import re # Biblioteca para expressões regulares 


board = chess.Board() 
pecas_unicode = {
    "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
    "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚"
}

def imprimir_tabuleiro_unicode(board):
    print()
    for linha in range(7, -1, -1):  # 8 até 1
        linha_str = f"{linha + 1} "
        for coluna in range(8):
            square = chess.square(coluna, linha)
            peca = board.piece_at(square)
            if peca:
                linha_str += pecas_unicode[peca.symbol()] + " "
            else:
                linha_str += ". "
        print(linha_str)
    print("  a b c d e f g h")

# Exemplo de uso
tabuleiro = imprimir_tabuleiro_unicode(board)
print(tabuleiro)



     
def movimento(origem, destino):
    try:
        print(f"Esses são os movimentos validos: {board.legal_moves}")
        origem = chess.parse_square(origem)
        destino = chess.parse_square(destino)
        movimento = chess.Move(origem, destino)
        if movimento in board.legal_moves:
            board.push(movimento)
            print(imprimir_tabuleiro_unicode(board))
        else:
            print("movimento inválido")
            print(imprimir_tabuleiro_unicode(board))
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

def converte_comando(texto):

    texto = texto.lower()
    texto = normalizar_numeros(texto)
    texto = texto.replace(" ", "").replace("para", "").replace("é", "e")
    match = re.match(r"([a-h][1-8])([a-h][1-8])", texto)
    if match:
        origem = match.group(1)
        destino = match.group(2)
        return origem + destino
    else:
        print(texto)
while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer.listen(mic)

        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            texto = texto.lower()
            comando = converte_comando(texto)
            if isinstance(comando, str):
                print(comando)
                movimento(comando[:2], comando[2:])
            else:
                print(f"movimento invalido: {texto}")
                continue
        except sr.UnknownValueError as erro:
            print("Não entendi o que você disse")
            recognizer
            continue