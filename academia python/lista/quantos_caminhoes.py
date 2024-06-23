def quantos_caminhoes(lista):
    soma = 0
    caminhoes = 0
    for el in lista:   
        soma += el
        limite = 2000
        
        if  soma > limite :
            caminhoes += 1
            soma = el   
    if soma > 0:
        caminhoes+=1
    return caminhoes
        
    

print(quantos_caminhoes([1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]))


        

