def calcula_tempo(dicionario):
    dicionario2 = {}
    for senha in dicionario.keys():
        a = dicionario[senha]
        t = (200/a) **(1/2)
        dicionario2[senha] = t
    return dicionario2

dic = {}
vencedor = ''
record = 0
nome = input('qual é seu nome ? ') 
while nome!= 'sair':
    aceleracao = float(input('qual a sua aceleracao? '))
    if nome not in dic:
        dic[nome] = 0 
    dic[nome] = aceleracao
    nome = input('qual é seu nome ? ')


dicionario = calcula_tempo(dic)
for nome,tempo in dicionario.items():
    if record == 0 :
        record = tempo
        vencedor = nome
    elif record > tempo:
        record = tempo
        vencedor = nome
    
print(f'O vencedor é {vencedor} com tempo de conclusão de {record} s')
        




