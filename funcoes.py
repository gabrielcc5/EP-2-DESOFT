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