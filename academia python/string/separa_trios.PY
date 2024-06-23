def separa_trios(l):
    lista = []
    lista2 = []
    for i in range(len(l)):
        if i%3 == 0 and i != 0:
            lista = []
        lista.append(l[i])
        lista2.append(lista[i])

        

    return lista

print(separa_trios(['João', 'Maria', 'Tiago', 'Pedro', 'Julia', 'Laura', 'Alice']))