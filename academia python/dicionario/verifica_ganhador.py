def verifica_ganhador(dici):
    for k in dici.keys():
        if dici[k] == []:
            return k
    return -1

