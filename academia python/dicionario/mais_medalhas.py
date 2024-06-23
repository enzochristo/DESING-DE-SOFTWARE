def mais_medalhas(l):
    d = {}
    maior = 0
    for info in l:
        nacional = info['nacionalidade']
        ouro = info['ouro']
        if nacional not in d:
            d[nacional] = 0
        d[nacional] += ouro
    for pais, qtd in d.items():
        if qtd > maior:
            maior = qtd
            res = pais
    return res

print(mais_medalhas([{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 23, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 9, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]))
        

        