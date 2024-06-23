import math
def entregador_mais_proximo(lista_rest,lista_posicao):

    dx = (lista_rest[0] - lista_posicao[0][0])**2
    dy = (lista_rest[1] - lista_posicao[0][1])**2

    menor_distancia = math.sqrt(dx + dy)

    for el in range(len(lista_posicao)):
        dx = (lista_rest[0] - lista_posicao[el][0])**2
        dy = (lista_rest[1] - lista_posicao[el][1])**2
        dxdy = math.sqrt(dx + dy)
        if dxdy < menor_distancia:
            menor_distancia = dxdy
            indice = el
    return indice

print(entregador_mais_proximo([3, 4],[
    [10, 20],
    [4, 2],
    [100, 74],
    [23, 63]
]))

        
        