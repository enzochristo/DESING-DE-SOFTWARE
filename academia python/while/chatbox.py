


continuar = True

while continuar : 

    comando = input('Digite algo: ')

    if comando == 'tchau' or comando == 'encerrar':
        print('Até logo')
        continuar = False

    elif comando == 'oi':
        print('Olá!')

    elif comando == 'bom dia':
        print('Bom dia')

    elif comando == 'site':
        print('Acesse https://insper.edu.br')

    elif comando == 'blackboard' :
        print('Lá temos materiais, notas e muito mais!')
    
    else: 
        print('Não sei como te ajudar!')

