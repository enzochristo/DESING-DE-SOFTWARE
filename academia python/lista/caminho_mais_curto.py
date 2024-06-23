import math
def caminho_mais_curto(l):
    liste = []
    i = 0
    for caminho in range(len(l)):
        dist = 0
        for ponto in range(len(l[caminho])-1):
            #x eh sempre index 0 e o y eh sempre o index 1
            x2 = l[caminho][ponto+1][0]
            x1 = l[caminho][ponto][0]
            y2 = l[caminho][ponto+1][1]
            y1 = l[caminho][ponto][1]
            dx = x1 - x2
            dy = y1 - y2
            dist += math.sqrt((dx)**2 + (dy)**2)
        liste.append(dist)
    menor = liste[0]
    while i < len(l):
        if menor > liste[i]:
            menor = liste[i]    
        i += 1
    return l[liste.index(menor)]





print(caminho_mais_curto([[[5, 2], [300, 1000], [10, 4]], [[5, 2], [3, 7], [7, 3], [10, 4]]]))



    

