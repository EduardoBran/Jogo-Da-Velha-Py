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


def funcao_verificar_vitoria():
    global velha
    vitoria = 'n'
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = 'n'

        # verificar vitória em linhas
        i_l = i_c = 0

        while i_l < 3:
            soma = 0
            i_c = 0
            while i_c < 3:
                if velha[i_l][i_c] == s:
                    soma += 1
                i_c += 1
            if soma == 3:
                vitoria = s
                break
            i_l += 1
        if vitoria != 'n':
            break

        # verificar vitória em colunas
        i_l = i_c = 0

        while i_c < 3:
            soma = 0
            i_l = 0
            while i_l < 3:
                if velha[i_l][i_c] == s:
                    soma += 1
                i_l += 1
            if soma == 3:
                vitoria = s
                break
            i_c += 1
        if vitoria != 'n':
            break

        # verifica diagonal 1
        soma = 0
        i_diag = 0
        while i_diag < 3:
            if velha[i_diag][i_diag] == s:
                soma += 1
            i_diag += 1
        if soma == 3:
            vitoria = s
            break

        # verifica diagonal 2
        soma = 0
        i_diagl = 0
        i_diagc = 2
        while i_diagc < 3:
            if velha[i_diagl][i_diagc] == s:
                soma += 1
            i_diagl += 1
            i_diagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria


tela()
# preciso jogada do jogador
jogador_joga()
# preciso jogada da cpu
cpu_joga()
# preciso verificar vitória (colocar break)
# redefinir o game
# loop se vai jogar novamente ou não
