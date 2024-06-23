dias = int(input('quantos dias quer analisar ? '))
i = 0
contador_frio = 0
contador_guarda_chuva = 0
contador_chuva = 0
contador_casaco = 0
while i < dias :
    i+= 1
    choveu = input('Choveu [S/N]')
    temperatura = int(input('Temperatura mínima (em Celsius)?'))
    guardachuva = input('Tinha guarda-chuva [S/N]?')
    casaco = input('Tinha casaco [S/N]?')
    if temperatura < 20 :
        contador_frio += 1
    if choveu == 'S':
        contador_chuva += 1
        if guardachuva == 'S':
         contador_guarda_chuva = contador_chuva
         
    if casaco == 'S' :
        contador_casaco += 1
print(f'Choveu em {contador_chuva} de {i} dias')
print(f'Fez frio em {contador_frio} de {i} dias')
print(f'Usou guarda-chuva em {contador_guarda_chuva} de {contador_chuva} dias de chuva')
print(f'Usou casaco em {contador_casaco} de {contador_frio} dias de frio')


