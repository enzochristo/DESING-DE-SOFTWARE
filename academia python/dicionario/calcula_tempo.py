
def calcula_tempo(dicionario):
    dicionario2 = {}
    for senha in dicionario.keys():
        a = dicionario[senha]
        t = (200/a) **(1/2)
        dicionario2[senha] = t
    return dicionario2

        
