def estritamente_crescente(lista):
    if lista == []:
        return lista
    maior = lista[0]
    crescente = [lista[0]]
    for el in lista:
        if el > maior :
            maior = el
            crescente.append(maior)
    return crescente


print(estritamente_crescente([1, 3, 2, 3, 4, 6, 5]))
        
