def numero_no_indice(l1):
    lista = []
    i = 0
    
    while i < len(l1):
        if l1[i] == i:
            lista.append(l1[i])
        i+=1
    return lista
print(numero_no_indice([1, 3, 7, 4]))