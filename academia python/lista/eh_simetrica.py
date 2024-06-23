#linha[i] linha[i+1] e coluna[i] = coluna[i+1] 
# deve ser ate o comprimento da linha
def simetrica(m):
    for el in range(len(m)):
         if len(m[el]) != len(m):
            return False
         else:
            continuar = True
    if continuar : 
        for col in range(1,len(m[0])):
         if col > 1:
            if somacoluna == somalinha:
                fim = True
            else: return False
         somacoluna = 0
         somalinha = 0
         for lin in range(col+1):
            somalinha += m[lin][col]
            somacoluna += m[lin][col]
    return fim


print(simetrica(
    [[1, 2, 3],
    [4, 5, 6],
    [9,8,7]]
    
))
                

                
        
        
        
        


        