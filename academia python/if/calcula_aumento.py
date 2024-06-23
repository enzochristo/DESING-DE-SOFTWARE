def calcula_aumento(salario): 
    if salario > 1250.00:
        aumento = .10 * salario
        return aumento 
    else :
        aumento = .15 * salario 
        return aumento 
    
a = float(input('salario '))

print(f'o aumento foi de {calcula_aumento(a)}')
