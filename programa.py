from funcoes import *
import random

frot = {
    "porta-av": [],
    "nav-tanq": [],
    "contratorp": [],
    "sub": [],
}

tips = [
    ("porta-av", 4, 1),
    ("nav-tanq", 3, 2),
    ("contratorp", 2, 3),
    ("sub", 1, 4)
]

for nm, tam, qtd in tips:
    for k in range(qtd):
        while True:
            print(f"Insira as informações referentes ao navio {nm} que possui tamanho {tam}")
            lin = int(input("Linha: "))
            while lin < 0 or lin > 9:
                print("Linha inválida!")
                lin = int(input("Linha: "))
            col = int(input("Coluna: "))
            while col < 0 or col > 9:
                print("Coluna inválida!")
                col = int(input("Coluna: "))
            if tam == 1:
                ori = "vertical"
            else:
                op = int(input("[1] Vertical [2] Horizontal >"))
                ori = "vertical" if op == 1 else "horizontal"
            if posicao_valida(frot, lin, col, ori, tam):
                preenche_frota(frot, nm, lin, col, ori, tam)
                break
            else:
                print("Esta posição não está válida!")

frot_op = {
    'porta-av': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'nav-tanq': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    'contratorp': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    'sub': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]
}

tab_op = posiciona_frota(frot_op)
tab_jog = posiciona_frota(frot)

jog_ant = []
impr = True

while True:
    if impr:
        print(monta_tabuleiros(tab_jog, tab_op))
    impr = True
    lin = int(input("Jogador, qual linha deseja atacar? "))
    while lin < 0 or lin > 9:
        print("Linha inválida!")
        lin = int(input("Jogador, qual linha deseja atacar? "))
    col = int(input("Jogador, qual coluna deseja atacar? "))
    while col < 0 or col > 9:
        print("Coluna inválida!")
        col = int(input("Jogador, qual coluna deseja atacar? "))
    if [lin, col] in jog_ant:
        print(f"A posição linha {lin} e coluna {col} já foi informada anteriormente!")
        impr = False
        continue
    jog_ant.append([lin, col])
    faz_jogada(tab_op, lin, col)
    if afundados(frot_op, tab_op) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        break
    while True:
        lin_op = random.randint(0, 9)
        col_op = random.randint(0, 9)
        if [lin_op, col_op] not in jog_ant:
            jog_ant.append([lin_op, col_op])
            break
    print(f"Seu oponente está atacando na linha {lin_op} e coluna {col_op}")
    faz_jogada(tab_jog, lin_op, col_op)
    if afundados(frot, tab_jog) == 10:
        print("Xi! O oponente derrubou toda a sua frota =(")
        break