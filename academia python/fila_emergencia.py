cor = input(' qual sua cor de pedido , vermelho , laranja ou azul ?')
qtd_vermelhos = int(input('quantos vermelhos estao aguardando ?'))
qtd_laranjas = int(input('quantos laranjas estao aguardando ?'))
qtd_azuis = int(input('quantos azuis estao aguardando ?'))
tempo_v = qtd_vermelhos*7
tempo_l = qtd_laranjas * 5
tempo_a = qtd_azuis * 5
tempo = 0 
if cor == 'V':
 tempo = tempo_v

if cor == 'L':
 tempo = tempo_v + tempo_l

if cor == 'A': 
 tempo = tempo_v + tempo_l + tempo_a

if not cor == 'L' and not cor == 'V' and not cor == 'A':
 tempo = None

print(tempo)

