
def total_do_semestre_por_bairro(dg):
    d2 = {}
    preco = 0
    for bairro, lista in dg.items():
        for i in range(6,12):
            preco += lista[i]
        d2[bairro] = preco
        preco = 0
    return d2



        