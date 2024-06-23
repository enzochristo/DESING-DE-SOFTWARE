def promocao_viagens(dest):
    d2 = {}
    for pais, lista in dest.items():
        posicao = lista[0]
        semd = lista[1]
        porcent = (posicao/10)
        comd = semd*(1 - porcent)
        d2[pais] = comd
    return d2


print(promocao_viagens({
    "Miami" : [1, 1000],
    "Ilhas Sandwich do Sul" : [4, 5000],
    "Barcelona" : [2, 2000],
    "Antártica" : [5, 200],
    "Buenos Aires" : [3, 500]
}))
        