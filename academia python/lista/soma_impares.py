def soma_impares(lista):
    i = 0
    soma = 0
    while i < len(lista):
        posicao = lista[i]
        if posicao % 2 != 0 :
         soma += lista[i]
        i += 1
    return soma
        
print(soma_impares([1,2,3]))
