continuar = True
while continuar:
    valor_desejado = input('digite um valor: ')
    if valor_desejado == '':
         print('-1')
         continuar = False
    else:
        valor_desejado = float(valor_desejado)
        if valor_desejado <= 0 :      
            print('erro de entrada')
        else:
            print(valor_desejado)
            continuar = False








    







    
    


    











