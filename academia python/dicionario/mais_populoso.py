def mais_populoso(d):
    dinv = {}
    max = 0
    soma = 0
    for estado,cidades in d.items():
        for populacao in cidades.values():
            soma += populacao
        dinv[soma] =  estado
        soma = 0
    for pop in dinv.keys():
        if pop > max:
            max = pop
    result = dinv[max]
    return result
print(mais_populoso({
    "São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
    "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}))
