def medias_por_inicial(d):
    d2 = {}
    for nome, nota in d.items():
        letra = nome[0]
        if letra not in d2:
            d2[letra] = [0,0]
        lista = d2[letra]
        lista = [d2[letra][0] + nota, d2[letra][1] + 1]
        d2[letra] = lista
    for inicial, soma in d2.items():
        media = soma[0]/soma[1]
        d2[inicial] = media
    return d2
print(medias_por_inicial({
    'Andrew Ayres': 6,
    'Fábio Ikeda': 10,
    'Fábio Kurauchi': 9,
    'Raul Hage': 8
 }))