def melhor_valor(ltroca , lestoque):
    soma = 0
    ds = {}
    for el in ltroca:
        for d in lestoque:
            if el == d['serial'] or el in d['equivalente']:
                if el not in ds:
                    ds[el] = d['valor']
                else: 
                    if ds[el] > d['valor']:
                        ds[el] = d['valor']
        if el not in ds:
            ds[el] = 0
        soma += ds[el]
    return soma





print(melhor_valor(['X1D', 'A3B'], [{'serial': 'A3B', 'valor': 198.7, 'equivalente': []},
    {'serial': 'XP2', 'valor': 190.9, 'equivalente': ['Z3Z', 'A3D']},
    {'serial': 'XP1', 'valor':   5.1, 'equivalente': ['TH5', 'TH6', 'X3D', 'X1D']}
]))

            
        









