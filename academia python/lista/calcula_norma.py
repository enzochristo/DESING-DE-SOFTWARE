import math
def calcula_norma(lista_componentes):
    soma = 0
    for el in lista_componentes:
        soma += el**(2)
    result = math.sqrt(soma)
    return result



def calcula_norma2(lista):
    soma = 0 
    i = 0 
    while i < len(lista):
        soma += lista[i]**2
        i +=1 
    result = math.sqrt(soma)
    return result

print(calcula_norma2([1,4,5,7]))
print(calcula_norma([1,4,5,7]))
    
