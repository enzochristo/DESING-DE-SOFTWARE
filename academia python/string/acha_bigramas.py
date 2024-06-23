def acha_bigramas(x):
    lista = []
    for i in range(len(x)-1):
        if x[i:2+i] not in lista:
            lista.append(x[i:i+2])
    return lista        
print(acha_bigramas('arroz'))
