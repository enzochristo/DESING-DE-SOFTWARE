from eh_primo import *

def primos_entre(a,b):
    numero = a 
    contador_primo = 0 
    continuar = True

    while continuar :
    
        if eh_primo(numero):
            contador_primo += 1
        elif  b  <= numero :
            continuar = False
            return contador_primo 
        numero += 1

print(primos_entre(10,100))
