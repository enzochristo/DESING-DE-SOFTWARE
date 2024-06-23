import random

aleat = random.randint(1,20)

contador = 1
numero = True

   

while numero :
    sorteio = int(input('escolha um numero de 1 a 20: '))
    if sorteio < aleat :
        print('Muito baixo')
        numero = True
    elif sorteio == aleat :
        print('Acertou') 
        numero = False
    elif sorteio > aleat:
        print('Muito alto')
        numero = True
    if numero : 
        contador += 1
    else: 
    
        print(contador)







"""
tem_duvidas = True
while tem_duvidas : 
    resposta_do_aluno = input('voce esta com duvidas ? ')
    if resposta_do_aluno == 'nao':
        print('parabens!')
        tem_duvidas = False
    else :
        print('pratique mais')

if tem_duvidas : 
    resposta_do_aluno = input('voce ainda tem duvidas ? ')
    if resposta_do_aluno == 'nao':
        tem_duvidas = False
        print('parabens')
    else:
        print('pratique mais')

if tem_duvidas : 
    resposta_do_aluno = input('voce ainda tem duvidas ? ')
    if resposta_do_aluno == 'nao':
        tem_duvidas = False
        print('parabens')
    else:
        print('pratique mais')
    
if tem_duvidas : 
    resposta_do_aluno = input('voce ainda tem duvidas ? ')
    if resposta_do_aluno == 'nao':
        tem_duvidas = False
        print('parabens')
    else:
        print('pratique mais')


if tem_duvidas : 
    resposta_do_aluno = input('voce ainda tem duvidas ? ')
    if resposta_do_aluno == 'nao':
        tem_duvidas = False
        print('parabens')
    else:
        print('pratique mais')
        print('ate logo')"""



"""tem_duvida = True

while tem_duvida:
    pergunta = input('voce tem duvida ? ')
    if pergunta == 'nao':
     tem_duvida = False
    else:
       print('pratique mais ')
   
    print('ate mais')   """    



