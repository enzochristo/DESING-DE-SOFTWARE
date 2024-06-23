def classifica_lista(lista):
    if len(lista) >= 2:
        contador = 1
        decres = 1
        for el in range(len(lista)-1):
            atual = lista[el]
            if lista[el+1] < atual:
                decres += 1
            if lista[el+1] > atual:
                contador += 1
        if contador == len(lista):
            return "crescente"
        if contador > 1 and decres >1:
            return 'nenhum'
        else:
            return 'decrescente'
    return 'nenhum'
        
print(classifica_lista([1,4]))
        


                


