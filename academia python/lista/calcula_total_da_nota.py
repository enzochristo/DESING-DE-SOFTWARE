"""def calcula_total_da_nota(precos,qtd):
    i = 0
    preco_final = 0
    while i < len(precos):
        preco_final += precos[i]*qtd[i]
        i += 1
    return preco_final
print(calcula_total_da_nota([10,5,2],[2,3,9]))"""

    
lista = [[1,2],[3,4],[5,6]]
i = 0
l2 = []

while i < len(lista):
    w = 1
    while w < len(lista[i]):
        l2.append([lista[i][w-1]+lista[i][w]])
        w+=1
    i+=1
print(l2)

lista = [1,2,3,4,5]
l2 = []
i = 0
while i <len(lista)-1:
    result = lista[i+1] - lista[i]
    l2.append(result)
    i+=1
print(l2)




