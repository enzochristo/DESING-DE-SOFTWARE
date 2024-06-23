dias = int(input('qual a quantidade de dias esperados ? '))
quantidade = 0
total = 0
menor_preco = 0
maior_preco = 0
contador_max = 1
contador_min = 1
quantidade_max = 1
quantidade_min = 1
lista = []

while dias != quantidade  :
    quantidade +=1
    preco = float(input('Qual foi o preco nesse dia ? '))

    if quantidade == 1 : 
        menor_preco = preco 
        maior_preco = preco 

    if menor_preco > preco : 
        menor_preco = preco
        contador_min = quantidade

    if maior_preco < preco : 
        maior_preco = preco
        contador_max = quantidade
   
    if preco in lista :
        if contador_max < quantidade :
            quantidade_max = contador_max
        elif contador_min < quantidade :
            quantidade_min = contador_min

    else:
        if menor_preco >= preco:
         quantidade_min = quantidade

        elif preco >= maior_preco :
         quantidade_max = quantidade
    lista.append(preco)
    
    

    total += preco

result = total / dias

print(f'O dia {quantidade_min} foi o melhor dia para compra')

print(f'O dia {quantidade_max} foi o pior dia para compra')

print(f'O preço médio cobrado foi de {result:.2f}')


