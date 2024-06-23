def valida_questao(d):
    d_ref = {'titulo':'oi','nivel':'oi','opcoes': 'oi','correta': 'oi'}
    d_errado = {}
    for chaves in d.keys():
        if chaves not in list(d_ref.keys()):
            if chaves == 'titulo':
            d_errado[chaves]
