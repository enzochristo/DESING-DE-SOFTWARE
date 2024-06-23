
numero = 1
numero_anterior = numero
contador_atual = 1
maior = contador_atual
maior_numero = numero

while numero_anterior<1000:
    par = numero % 2 == 0

    if par:
        numero= numero/2
        contador_atual+=1

    else:
        numero =3 * numero + 1
        contador_atual+=1

    if numero == 1:
        if contador_atual>maior:
            maior = contador_atual
            maior_numero = numero_anterior
        contador_atual = 1
        numero_anterior+=1
        numero = numero_anterior
        
print(maior_numero)
print(maior)
            




    



