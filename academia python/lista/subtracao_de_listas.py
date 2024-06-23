#programa que roda o oposto da interseccao de ambas as listas

def subtracao_de_listas(l1,l2):
    i = 0
    l3 = []
    l4 = []
    if len(l1) > len(l2):
        maior_lista = l1
        menor_lista = l2
    else:
        maior_lista = l2
        menor_lista = l1

    while i < len(menor_lista) :
        if maior_lista[i] not in menor_lista:
            l3.append(maior_lista[i])
        if menor_lista[i] not in maior_lista:
            l4.append(menor_lista[i])
        i += 1
    l5 = l3 + l4
                      
    return l5

print(subtracao_de_listas([2, 7, 3.1, 'banana'], [2, 'banana', 'carro']))

    
def subtracao_de_listas(l1,l2):
    i = 0
    l3 = [ ]
    while i < len(l1):
        if l1[i] not in l2 :
            l3.append(l1[i])
        i += 1
    return l3

print(subtracao_de_listas([2, 7, 3.1, 'banana'], [2, 'banana', 'carro','oi','a']))

