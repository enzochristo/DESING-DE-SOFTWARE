def soma_valores(lista):
    contador = 0 
    soma = 0
    tamanho = len(lista)
    while contador < tamanho:
        soma += lista[contador]
        contador +=1
    return soma