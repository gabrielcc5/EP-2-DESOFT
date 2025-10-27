
def define_posicoes(linha, coluna, orientacao, tamanho):
    l_posi = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            l_posi.append([linha + i, coluna])
    else:  
        for i in range(tamanho):
            l_posi.append([linha, coluna + i])
    
    return l_posi 