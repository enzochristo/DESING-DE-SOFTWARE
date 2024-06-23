
v = float(input('qual a velocidade ? '))

if v > 80:
    multa  = (v - 80)*5
    print('vc foi multado! o valor a pagar é de {0:.2f}'.format(multa))
else:
    print('nao foi multado')


   
