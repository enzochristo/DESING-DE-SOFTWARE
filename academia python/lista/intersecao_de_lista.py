def intersecao_de_lista(l1,l2):
    maior = 0
    menor = 0
    if len(l1) < len(l2):
        maior = l2
        menor = l1
    menor = l2
    maior = l1
    l3 = []
    for el in range(len(menor)):
            for int in range(len(maior)):
             if menor[el] == maior[int]:
                 l3.append(menor[el])
    return l3

print(intersecao_de_lista([2, 7, 3.1, 'banana'],[2, 'banana', 'carro']))
                
def intersecao_de_lista(l1,l2):
    maior = 0
    menor = 0
    if len(l1) < len(l2):
        maior = l2
        menor = l1
    menor = l2
    maior = l1
    i = -1
    a = 0
    n = 0
    l3 = []
    while i < len(menor) -1 :
        i+=1
        a = 0
        while a < len(maior):
         if menor[i] == maior[a]:
            l3.append(menor[i])
         a+=1
    return l3
         
        

                 
print(intersecao_de_lista([2, 7, 3.1, 'banana'],[2, 'banana', 'carro']))