def eh_primo(numero):
    divisor = 1
    e_primo = True
    if numero <=1 :
            return False
    while divisor < numero :
        divisor +=1
        resto = numero % divisor
        if (numero != divisor) and resto == 0  :
            e_primo = False
            return e_primo
    return e_primo


def primos_gemeos(n):
    a = 3
    i = 0
    soma = 0
    b = 5
    while i < n:
            while eh_primo(a) != True or eh_primo(b) != True or b - a != 2:
             a+=2
             b+=2
            soma += ((1/a) + (1/b))
            a += 2
            b += 2
            i += 1
    return soma



   

print(primos_gemeos(1/3+1/5))