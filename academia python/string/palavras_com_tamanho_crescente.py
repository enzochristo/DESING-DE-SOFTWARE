def palavras_com_tamanho_crescente(ls):
    for i in range(1,len(ls)):
        if len(ls[i]) > len(ls[i-1]):
            resp = True
        else:
            return False
    return True