def PiWallis(n):
    termo_par = 0
    contadorimpar = 0
    contador = 1
    produto = 1

    while contador < n :
        if contador % 2 != 0 :
            termo_par = termo_par +2
            contadorimpar = termo_par - 1
            


        if contador % 2 == 0:
            
            contadorimpar = termo_par + 1

        produto *= termo_par/contadorimpar
        contador+=1
    return produto*2

print(PiWallis(6))


    
           