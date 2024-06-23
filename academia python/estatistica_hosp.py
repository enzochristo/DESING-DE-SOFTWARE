total = 0 
continuar = True
estatistica = 0 
contador_11 = 0
contador_17 = 0
contador_25 = 0
contador_35 = 0 
contador_59 = 0
contador_60 = 0
contador = 0
while continuar:
    numero = int(input('qual a idade do paciente ? '))
    if numero >=0 :
     contador += 1

     
    total = contador
    if 0 <= numero <= 11 :
        contador_11 += 1
        

    if 12 <= numero <= 17 :
        contador_17 += 1
             

    if 18 <= numero <= 25 :
        contador_25 += 1
          

    if 26 <= numero <= 35:
        contador_35 += 1
        

    if 36 <= numero <= 59:
        contador_59 += 1
         

    if numero > 60 :
        contador_60 += 1
        

    if numero < 0 :
        continuar = False
        ate_11 = (contador_11/total)*100
        ate_17 = (contador_17/total)*100
        ate_25 = (contador_25/total)*100
        ate_35 = (contador_35/total)*100
        ate_59 = (contador_59/total)*100
        acima_60 = (contador_60/total)*100

        print('0-11 anos: {0: .2f} %'.format(ate_11))
        print('12-17 anos: {0: .2f} %'.format(ate_17))
        print('18-25 anos: {0: .2f} %'.format(ate_25))
        print('26-35 anos: {0: .2f} %'.format(ate_35))
        print('36-59 anos: {0: .2f} %'.format(ate_59))
        print('acima de 60 anos: {0: .2f} %'.format(acima_60))
       


