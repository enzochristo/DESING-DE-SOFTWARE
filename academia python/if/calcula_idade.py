def calcula_idade (dia , mes , ano , dia_a , mes_a , ano_a):
    x = ano_a - ano
    if (mes > mes_a) or (mes == mes_a and dia > dia):
        x = x - 1
        return x





 

dia = int(input('que dia é seu niver ? '))
mes = int(input('que mes é seu niver ? '))
ano = int(input('que ano é seu niver ? '))
dia_a = int(input('que dia é hoje ? '))
mes_a = int(input('que mes é hoje ? '))
ano_a = int(input('que ano é hoje ? '))

print(f'sua idade é {calcula_idade(dia , mes , ano , dia_a ,mes_a, ano_a)}')
