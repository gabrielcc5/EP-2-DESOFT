# EX 1

def define_posicoes(linha, coluna, orientacao, tamanho):
    l_posi = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            l_posi.append([linha + i, coluna])
    else:  
        for i in range(tamanho):
            l_posi.append([linha, coluna + i])
    
    return l_posi 


#EX 2
def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    p = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome not in frota:
        frota[nome] = [p]
    else:
        frota[nome].append(p)
    
    return frota

#EX 3
def faz_jogada(tab, l, col):
    if tab[l][col] == 1:
        tab[l][col] = 'X'  
    else:
        tab[l][col] = '-' 
    return tab

#EX 4
def posiciona_frota(frota):
    tab = []
    for i in range(10):
        l = []
        for j in range(10):
            l.append(0)
        tab.append(l)
    for nome in frota:
        for posicoes in frota[nome]:
            for l, col in posicoes:
                tab[l][col] = 1

    return tab

#EX 5
def afundados(frota, tab):
    nav_afundados = 0

    for nome in frota:
        for posicoes in frota[nome]:
            afundado = True
            for l, col in posicoes:
                if tab[l][col] != 'X':
                    afundado = False
                    break
            if afundado:
                nav_afundados += 1

    return nav_afundados

#EX 6
def posicao_valida(frota, l, col, orient, tam):
    novas_posicoes = define_posicoes(l, col, orient, tam)

    # valida limites do tabuleiro
    for lin, col in novas_posicoes:
        if lin < 0 or lin >= 10 or col < 0 or col >= 10:
            return False

    # valida sobreposicao com a frota existente
    for nome in frota:
        for pos in frota[nome]:
            for lin, col in pos:
                if [lin, col] in novas_posicoes:
                    return False

    return True 

#EX 8
def posicoesbuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  join([str7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        
    return texto

