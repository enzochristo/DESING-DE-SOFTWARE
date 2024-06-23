def monta_dicionario(l1,l2):
    dicionario = {}
    for index in range(len(l1)):
        dicionario[l1[index]] = l2[index]     
    return dicionario
