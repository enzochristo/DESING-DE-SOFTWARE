def eh_primo(numero):
    divisor = 1
    e_primo = True
    #resto = numero % divisor
    if numero <= 1 :
        return False
    while divisor < numero :
        divisor += 1
        resto = numero % divisor #o resto tem que estar dentro do loop para que a divisao comece necessariamente com o 2 , caso coloque fora do while , ele vai comecar a divisao com 1
        if (numero != divisor) and resto == 0  :  #coloquei parenteses(sem necessidade) mas para evidenciar que esse tem que -necessariamente- ser "lido" antes
            e_primo = False
            return e_primo
    return e_primo

print(eh_primo(7))
        