import speech_recognition as sr # Biblioteca para reconhecimeto de voz
import chess # Biblioteca para manipulação de xadrez
import re # Biblioteca para expressões regulares 


board = chess.Board() # Cria o tabuleiro de xadrez padrão utilizando a biblioteca chess
pecas_unicode = {
    "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
    "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚"
} # Dicionário para estilizar o tabuleiro 

def imprimir_tabuleiro_unicode(board): # função para imprimir o tabuleiro estilizado usando o dicionário anterior 
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


tabuleiro = imprimir_tabuleiro_unicode(board) # cria uma variável para guarda o tabuleiro estilizado  
print(tabuleiro)



     
def movimento(origem, destino): # Função para realizar o movimento das peças no tabuleiro
    try:
        print(f"Esses são os movimentos validos: {board.legal_moves}") # Mostra os movimentos possiveis 
        origem = chess.parse_square(origem) # Guarda a posição de origem da peça
        destino = chess.parse_square(destino) # Guarda o destino da peça 
        movimento = chess.Move(origem, destino) # Guarda o movimeto que a peça irá realizar 
        if movimento in board.legal_moves: # Verifica se o movimento é válido (se o comando dado está de acordo com os movimentos possíveis)
            board.push(movimento) # Realiza o movimento
            print(imprimir_tabuleiro_unicode(board)) # Imprime o tabuleiro após a jogada 
            vez = "BRANCAS" if board.turn else "PRETAS" # Verifica de quem é a vez de jogar 
            print(f"Agora é a vez das {vez}") # Mostra ao usuário de quem é a vez de jogar BRANCAS ou PRETAS 
        else: # Condição caso o movimento não seja válido 
            print("movimento inválido") # Mostra ao usuário que o movimento é inválido
            print(imprimir_tabuleiro_unicode(board)) # Imprime o tabuleiro atual 
    except ValueError as e: # Exceção para capturar erros de valor, como coordenadas inválidas
        print(f"movimento irreconhecido (lista inválida)")    



recognizer = sr.Recognizer() # Cria um objeto para reconhecimento de voz 

def normalizar_numeros(texto): # Função para transformar palavras em números 
    numeros = {
        "um": "1", "dois": "2", "três": "3", "tres": "3",
        "quatro": "4", "cinco": "5", "seis": "6",
        "sete": "7", "oito": "8"
    } # dicionário que guarda as palavras e seus respectivos números 
    for palavra, numero in numeros.items(): # Laço para substituir as palavras pelos os números
        texto = texto.replace(palavra, numero)
    return texto

def converte_comando(texto): # Função para converter o comando de voz em movimento no tabuleiro 

    texto = texto.lower() # Transforma todas as letras em minúsculas
    texto = normalizar_numeros(texto) # Normaliza os números de palavras para números usando a funçao anterior 
    texto = texto.replace(" ", "").replace("para", "").replace("é", "e") # susbtitui espaços, "para" e "é" por "e"
    match = re.match(r"([a-h][1-8])([a-h][1-8])", texto) # Expressão regular para capturar o movimento no formato origem-destino, como "e2e4"
    if match: # Verifica se o texto corresponde ao padrão esperado
        origem = match.group(1) # Captura a origem da peça
        destino = match.group(2) # captura o destino da peça 
        return origem + destino # Retorna o comando no formanto origem-destino
    else: # Se o texto não corresponder ao padrão esperado, retora erro 
        print(f"erro:{texto}")
while True: # Loop infinito para continuar ouvindo comando de voz 
    with sr.Microphone() as mic: # Cria um onjeto de microfone para capturar o áudio 
        recognizer.adjust_for_ambient_noise(mic, duration=0.3) # Ajusta o reconhecimento de voz
        audio = recognizer.listen(mic) # Escuta o áudio do microfone

        try: # Tenta reconhecer o áudio capturado
            texto = recognizer.recognize_google(audio, language='pt-BR') # Usa o Google para reconhecer o áudio em português
            texto = texto.lower() # transforma o texto reconhecido em letras minúsculas
            comando = converte_comando(texto) # Converte o texto reconhecido em um comando de movimento no tabuleiro
            if isinstance(comando, str): # Verifica se o comando é uma String
                print(comando) # Imprime o comando que foi dito
                movimento(comando[:2], comando[2:]) # Realia o movimento no tabuleiro usando a função movimento
            elif texto == "para" or texto == "parar": # Para o jogo quando dito "para" pelo o usuário
                 print("jogo encerrado")
                 break
            else:
                print(f"movimento invalido: {texto}")
                continue
            
        except sr.UnknownValueError as erro:
            print("Não entendi o que você disse")
            recognizer
            continue