def filtra_bagagens(lista,al,ll,pl):
    result = 0
    for el in range(len(lista)):
        if lista[el][0] > al or lista[el][1] > ll or lista[el][2] > pl:
            result += 1
    return result 

print(filtra_bagagens([[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]], 55, 35, 25))