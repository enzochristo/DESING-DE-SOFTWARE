def seleciona_candidatos(candidatos,criterios):
    if candidatos == []:
        return candidatos
    result = 0
    aprovados = []
    notas = candidatos[0][2]
    for el in range(len(candidatos)):
        if len(candidatos[el][2]) == 3:
            for nota in range(len(notas)):
                if candidatos[el][2][nota] >= criterios[nota]:
                    result +=1
            if result == 3:
                 del(candidatos[el][2])
                 aprovados.append(candidatos[el])
            result = 0

           
    return aprovados


print(seleciona_candidatos([
    ['Julia WA.', '6780-9', [10.0, 9.5, 7.5]],
    ['Bruna QS.', '3423-1', [10.0, 9.2, 7.4, 9.5]],
    ['Camila A.', '7621-5', [9.00, 8.0, 8.3]],
    ['Vizeu BA.', '4040-4', [9.00, 9.1]],
    ['Hamil KS.', '2362-0', [9.00, 8.1, 8.0]],
    ['Igor VGS.', '7877-1', [4.90, 8.1, 8.0]],
],[5.0, 8.0, 7.0]))
