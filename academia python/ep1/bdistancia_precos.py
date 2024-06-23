import math
def distancia(lista):
 pt1 = 0
 pt2 = 0

 for el in range(len(lista)):
        wish = lista[el]
        for posicao in range(1):
         venda = wish[posicao+1]
         desejado = wish[posicao]
         pt1 += (desejado - venda)**2

 pt2 = math.sqrt(pt1/(el+1))

 return pt2
