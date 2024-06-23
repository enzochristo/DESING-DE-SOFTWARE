tamanho = input('qual o tamanho do bolo ? ')
saldo =int(input('qual o orcamento do cliente ? '))
preco = 0 
if tamanho == 'XG':
    preco = 50
elif tamanho == 'G':
    preco = 31
elif tamanho == 'M':
    preco = 20
elif tamanho == 'P':
    preco = 7
elif tamanho == 'XP':
    preco = 5

qtd_bolos = saldo // preco

resto = saldo % preco 

premio_c= resto // 2

premio_b = resto % 2


if qtd_bolos <= 4 and resto !=0 :

    if premio_c != 0 : 
        print(f'{premio_c} cheesecake')
    if premio_b != 0 :
        print(f'{premio_b} brownie')
elif resto == 0 :
 print('sem acompanhamento' )
else:
    if premio_c !=0 :
      print(f'{premio_c} cupcake')
    if premio_b != 0 :
      print(f'{premio_b} banoffee')







