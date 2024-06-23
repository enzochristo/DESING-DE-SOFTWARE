def inverte_dicionario(d):
    dinv = {}
    lista = []
    a = []
    for nome, idade in d.items():
        if idade not in dinv:
            dinv[idade] = [nome]
        else:
            lista2 = dinv[idade] # lista dentro do dicionario 
            lista2.append(nome) # appendando o valor dentro da propria lista do dicionario, pois ali ela ja existe e esta fixa.
            dinv[idade] = lista2
    return dinv

#para que a lista nao seja alterada, deve ser inserido o valor dentro da lista dentro do dicionario 




    return dinv


   

print(inverte_dicionario({'Ana': 19, 'Bruno': 18, 'João': 19}))