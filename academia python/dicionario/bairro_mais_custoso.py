def total_do_semestre_por_bairro(dg):
    d2 = {}
    preco = 0
    for bairro, lista in dg.items():
        for i in range(6,12):
            preco += lista[i]
        d2[bairro] = preco
        preco = 0
    return d2

result = total_do_semestre_por_bairro({
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
})


def bairro_mais_custoso(d):
    max = 0
    ganhador = '' 
    for bairro, valor in d.items():
        if valor > max:
            max = valor
            ganhador = bairro
    return ganhador

print(bairro_mais_custoso(result))


