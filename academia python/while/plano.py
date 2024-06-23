
plano = input('qual o seu plano?')
serie = input('qual série gostaria de assistir?')
i = 0
while serie != 'sair' :      
    series = ['stranger things','friends','the circle','mad men','brasileirao','champions']
    plano_novo =  series[2],series[3]
    plano_padrao = series[0],series[1],series[2],series[3]

    if serie not in series:
        print('Serie inexistente!')
    else:
        
     mensagem_better = 'Precisa comprar novo plano!'

     if plano =='novo':
        if serie in plano_novo:
            print('Ok, reproduzindo!\nNum oferecimento de DesSoft!')
        else:print(mensagem_better)

     if plano =='padrao':
        if serie in plano_padrao:
                print('Ok, reproduzindo!')
        else:print(mensagem_better)


     if plano =='premium':
        if serie in series:
                    print('Ok, reproduzindo!')
        else:print(mensagem_better)


    serie = input('qual série gostaria de assistir?')
                 

print('Ok, tchau!')
