import os
import random
from colorama import Fore, Back, Style

jogar_novamente = 's'
jogadas = 0
quem_joga = 2  # 1 cpu | 2 jogador
max_jogadas = 9
verificar_vitoria = 'n'

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# funcao que vai limpar a tela e desenhaar a matriz com as jogadas
def tela():
    global velha
    global jogadas
    os.system('cls')

    print("   0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])

    print('\nJogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)

while True:
    tela()
    # preciso jogada do jogador
    # preciso jogada da cpu
    # preciso verificar vitória (colocar break)
    # redefinir o game
    # loop se vai jogar novamente ou não