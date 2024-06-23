
def elevado(x):
    result = x ** 2
    return result



def raiz_quadrada(n):
    impar = 1
    sub = n- impar
    contador = 1 
    continuar = True
    while continuar :
        impar += 2 
        contador += 1 
        sub -= impar
        if sub == 0 : 
            continuar = False
            return contador
    
elevar = elevado(81)
print(elevar)
print(raiz_quadrada(elevar))
        







