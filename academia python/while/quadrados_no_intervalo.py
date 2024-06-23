def quadrados_no_intervalo(a,b):
    if a > b :
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    i = 0
    qdp = 0
    while i < maior-menor+1:
        numero = (menor+i)
        interesse = int(numero ** (1/2))
        i += 1
        if numero  == interesse **2 :
            qdp += 1
    return qdp
print(quadrados_no_intervalo(1,5))