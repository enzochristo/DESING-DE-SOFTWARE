def minimos_colunas(matriz):
    resp = []
    menor_valor = 0
    w = 0
    menor_valor= matriz[0][0]

    while i < len(matriz[0])-1:
            if menor_valor > matriz[i][w]:
              menor_valor = matriz[i][w]
            i += 1
    w +=1
    while w < len(matriz):
        i = 0
        
            



print(minimos_colunas([
    [2, 4, -1, 3],
    [0, 7, 6, 4],
    [8, 1, 2, 3]
]))







"""resp = []
def funcao(lista,delta):
    for el in range(delta-1,len(lista)):
        resp.append((lista[el] - lista[el-delta+1])/lista[el-delta+1])
    return resp
    
print(funcao([5,4,6,3,5],3))"""









            
     


          


        

   
