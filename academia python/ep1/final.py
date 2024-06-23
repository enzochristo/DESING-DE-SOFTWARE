
valor_desejado = input('valor desejado: ')
if valor_desejado != '':
    valor_venda = input('valor venda: ')

lista1 = [ ]
contador = 0
soma_desejado = 0
soma_venda = 0
desv_pad_desejado = 0
desv_pad_venda = 0

import math
def distancia(lista):
 pt1 = 0
 pt2 = 0

 for el in range(len(lista)):
        wish = lista[el]
        for posicao in range(len(lista[0])-1):
         venda = wish[posicao+1]
         desejado = wish[posicao]
         pt1 += (desejado - venda)**2

 pt2 = math.sqrt(pt1/(el+1))

 return pt2



while  valor_desejado != '' and valor_venda != '' :

    valor_desejado = float(valor_desejado)
    valor_venda = float(valor_venda)
    condicao = valor_venda >= valor_desejado
    

    if valor_desejado >= 0 and valor_venda >= 0  :
        if condicao:
            lista1.append([valor_desejado,valor_venda])
            soma_desejado += lista1[contador][0]
            soma_venda += lista1[contador][1]
            contador += 1
        else:
            print('entradas desconsideradas pois valor desejado maior que o valor da venda, tente novamente!')
        
    valor_desejado = input('valor desejado: ')

    if valor_desejado != '':
        valor_venda = input('valor venda: ')

soma_desejado /= contador
soma_venda /= contador

for el in range(len(lista1)):
   desv_pad_desejado += (lista1[el][0] - soma_desejado)**2
   desv_pad_venda += (lista1[el][1] - soma_venda)**2

if distancia(lista1) > .05 * soma_desejado:
    anomalia = 'SIM'
else: anomalia = 'NÃO'


desv_pad_desejado = math.sqrt(desv_pad_desejado/el)
desv_pad_venda = math.sqrt(desv_pad_venda/el)

print(f'MÉDIA: desejado [{soma_desejado:.2f}] venda [{soma_venda:.2f}]')
print(f'DESVIO PADRÃO AMOSTRAL: desejado [{desv_pad_desejado:.2f}] venda [{desv_pad_venda:.2f}]')
print(f'Anomalia:{anomalia}')







    
    



   

