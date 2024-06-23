

def minimo(matriz):
    col = 0
    linha = 0
    resp = []
    while col <len(matriz[0]):
        menor = matriz[linha][col]
        while linha <len(matriz):
            if menor>matriz[linha][col]:
                menor = matriz[linha][col]
            linha+=1
        col+=1
        resp.append(menor)
        linha = 0
    return resp


lista = [ 
    [5],
    [-1]
]
print(minimo(lista))

