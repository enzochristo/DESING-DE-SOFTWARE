def decimal_para_binario(n):

    numero = 0
    interesse = ''
    if n > 0:
        while numero <= len(n):
            numero += 1
            divisor = numero
            numero = numero//2
            resto = divisor%2
            interesse += str(resto)

    inv = ''
    i = 1
    while i <= len(n):
        

           

               

        


print(decimal_para_binario(20))