mes_escolhido = input('qual o mes? ')

meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

if mes_escolhido <= 12 or mes_escolhido >= 1:
    print(meses[mes_escolhido])
