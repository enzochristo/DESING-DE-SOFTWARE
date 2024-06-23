def quadrado_magico(matriz):
    soma_linhas = 0
    soma_colunas = 0
    soma_diag = 0
    referencia_coluna = 0
    referencia_linha = 0
    referencia_diag = 0
    for coluna in range(len(matriz[0])):
        for linha in range(len(matriz)):
            soma_colunas += matriz[linha][coluna]
    return soma_colunas

print(quadrado_magico([[1,2],[3,4]]))
        
    


