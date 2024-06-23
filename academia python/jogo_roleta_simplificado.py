import random 

saldo = 100 
while saldo > 0:
    print(saldo)
    aposta = int(input('aposta'))
    if aposta == 0 : break
    sorteado = random.randint(0,36)
    if input('tipo ? ') == 'n':
        #numero
        escolhido = int(input('numero : '))
        if escolhido == sorteado:
            saldo += 35 * aposta
        else: 
            saldo -= aposta
    else:
            #paridade
            esc_par = input('p ou i ? ') == 'p'
            if(sorteado % 2 == 0 and esc_par ) or (sorteado % 2 != 0 and not esc_par) :
                saldo += aposta
            else : 
                saldo -= aposta