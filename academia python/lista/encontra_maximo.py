import math
def encontra_maximo(lista):
    maior_col = lista[0][0]
    linha = 0
    while linha < len(lista):
        col = 0 
        while col < len(lista[0]):
            if math.sqrt((lista[linha][col])**2) > math.sqrt(maior_col**2):
                maior_col = lista[linha][col]
            col += 1
        linha += 1
    return maior_col

print(encontra_maximo([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))