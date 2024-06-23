def calcula_troco(valor,pago,lista):
    lista_troco = []
    troco = pago - valor
    for el in lista:
        if el <= troco:
            quantidade = troco//el
            if troco >= 2:
                lista_troco.append(f'{quantidade:.0f} nota(s)deR${el}')
            elif troco < 2 and troco != 0:
                lista_troco.append(f'{quantidade:.0f} moeda(s)deR${el}')
            troco = troco%el
    return lista_troco
    




print(calcula_troco(2.25,1000,[100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]))

            