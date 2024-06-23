def inverte_lista(lista):
    invertido = []
    inicio = len(lista)-1
    for el in range(inicio,-1,-1):
        invertido.append(lista[el])
    return invertido

print(inverte_lista([1,2,3,4,5]))