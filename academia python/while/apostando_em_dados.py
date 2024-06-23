#o jogador escolhe um número da sorte, um valor para aposta e 
#o número de rodadas que irá simular,
# passando então esses valores, nessa ordem, como parâmetros para a função de simulação que você vai criar

import random

def apostando_em_dados(n_sorte,aposta,rodadas):
    contador = 0
    while contador < rodadas:
        contador +=1
        sorteado = random.randint(1,6)

        if n_sorte == sorteado:
            aposta *= (1+1/3)

        else :
            aposta *= (1-1/6)

        valor_resultante = aposta
       #aposta = valor_resultante

    return valor_resultante

print(apostando_em_dados(5,180,3))