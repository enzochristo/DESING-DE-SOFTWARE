preco_p = 0
acres = 0
tam = input('Tamanho [P/M/G]? ') 
if tam == 'P' :
    preco_p = 50.00
elif tam == 'M' :
    preco_p = 70.00
else :
    preco_p = 90.00

if input('Borda recheada [S/N]?') == 'S':
    acres = .15 * preco_p

if input('Adicional de queijo [S/N]?') == 'S':
    acres = acres + (preco_p * .1)

if input('Refrigerante [S/N]?') == 'S':
    acres += 12
a = input('Sobremesa [S/N]?')
if a == 'S':
    acres = acres + 20
    
preco = preco_p + acres

if tam == 'G' and a == 'S' :
    preco *= .93

print(f'{preco:.2f}')