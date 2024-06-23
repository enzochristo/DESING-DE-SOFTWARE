
def eh_identidade(lista):
    diagonalprincipal = []
    if len(lista) != len(lista[0]):
        return False
    else:
        for linha in range(len(lista)):
            for coluna in range(len(lista[0])):
                 if linha != coluna and lista[linha][coluna]!= 0 :
                     return False
                 if linha == coluna and lista[linha][coluna] != 1:
                    return False

    return True



            
    

print(eh_identidade([[11,0],[1,1]]))

