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

    print('')
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])

    print('\nJogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogador_joga():
    global jogadas
    global quem_joga
    global max_jogadas

    if quem_joga == 2 and jogadas < max_jogadas:

        try:
            l = int(input('\nLinha..: '))
            c = int(input('Coluna.: '))
        except ValueError as e:
            print(f'VALOR INVÁLIDO -> {e}')
            os.system('pause')
            return

        try:
            while velha[l][c] != " ":
                print('\nCampo ocupado. Tente outro...')
                os.system('pause')
                l = int(input('\nLinha..: '))
                c = int(input('Coluna.: '))
            velha[l][c] = "X"
            quem_joga = 1
            jogadas += 1
        except Exception as e:
            print('\nLinha e/ou coluna inválida.')


def cpu_joga():
    global jogadas
    global quem_joga
    global max_jogadas

    if quem_joga == 1 and jogadas < max_jogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)

        velha[l][c] = 'O'
        jogadas += 1
        quem_joga = 2


while True:
    tela()
    # preciso jogada do jogador
    jogador_joga()
    # preciso jogada da cpu
    cpu_joga()
    # preciso verificar vitória (colocar break)
    # redefinir o game
    # loop se vai jogar novamente ou não
