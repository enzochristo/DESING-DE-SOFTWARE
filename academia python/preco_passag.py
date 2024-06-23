def viagem(km):
       if km > 200:
              preco = 200*.5 + .45(km-200)
       else :
              preco = km *.5

       return preco

a = float(input('distancia '))

print(f'viagem(a):.2f')


#'{0:.1f}, {1:.4f}'.format(1.23456, 7.89123) - exemplo
