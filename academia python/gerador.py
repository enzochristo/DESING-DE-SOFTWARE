import random
def eh_primo(numero):
    divisor = 1
    e_primo = True
    if numero <= 1 :
        return False
    while divisor < numero :
        divisor += 1
        resto = numero % divisor 
        if (numero != divisor) and resto == 0  :
            e_primo = False
            return e_primo
    return e_primo

def gerador(n1,n2):
    continuar = True
    if n1 <=1 or (n2-n1) < 1000: 
        return 'erro de intervalo'
    else : 
        while continuar:
            numero = random.randint(n1,n2)
            if eh_primo(numero): 
                return numero
    
random.seed(37)
print(gerador(500,6000))
        

