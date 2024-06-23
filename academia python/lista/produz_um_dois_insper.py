def produz_um_dois_insper(numero_inicial,numero_final,multiplo):
    lista = []
    for el in range(numero_inicial,numero_final+1):
        if el % multiplo == 0:
            lista.append("Insper")
        else:
            lista.append(el)
    return lista

print(produz_um_dois_insper(2,13,3))
            