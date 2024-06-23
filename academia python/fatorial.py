


def fatorial(n):
    continuar = True
    result = 1 
    contador = 0 
    while continuar :   
        contador +=1
        result *= contador
        if contador >= n :
            continuar = False
            return result
        
print(fatorial(0))
        
        

        
        