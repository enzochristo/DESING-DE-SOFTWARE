def calcula_overbooking(capacidade,lista_passagens_vendidas):
    soma = 0
    if lista_passagens_vendidas == []:
        return 0
    for el in  lista_passagens_vendidas:
        if el > capacidade:
            soma += el - capacidade
    return soma

print(calcula_overbooking(72, [80, 65, 77, 53, 47]))


