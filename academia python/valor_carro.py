valor_carro = int(input('Valor do carro na FIPE ? '))

idade = input('Condutor principal é menor de 25 anos ? ')

servico = input('Servico de guincho para fora da cidade ? ')

local = input('Local de pernoite? ')

sinistro = input('Tem sinistro anterior?')

quantos = int(input('Quantos? '))

valor_base = .04*valor_carro
taxa = 0
if valor_carro >= 40001 and valor_carro <=90000:
    valor_base = .05*valor_carro
if valor_carro >=90001:
    valor_base = 0.075*valor_carro

if idade == 'N' :
    valor_base_1 = valor_base * 1.2
if servico == 'S':
    taxa = 110
if local == 'rua':
    valor_base_1 = valor_base * 1.15
if sinistro == "N":
    valor_base_1= valor_base * .92
    
else :
  valor_base_1 = valor_base * (1.03 **quantos)

valor_total = valor_base_1


if idade == 'S' and local == 'garagem':
 valor_total = valor_total * .88

print('{0: .2f}'.format(valor_total))


