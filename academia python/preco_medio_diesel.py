dias = int(input('qual a quantidade de dias esperados ? '))
quantidade = 0 
total = 0

while dias != quantidade :
    quantidade +=1
    preco = float(input('Qual foi o preco nesse dia ? '))
    total += preco

result = total / dias
print('{0: .2f}'.format(result))







