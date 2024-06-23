def agrupa_por_nacionalidade(d_atletas):
    d_nomes = {}
    for nome in d_atletas.keys():
        nacionalidade = d_atletas[nome]['nacionalidade']
        if nacionalidade not in d_nomes:
            d_nomes[nacionalidade] = []
        d_nomes[nacionalidade].append(nome)
    return d_nomes

print(agrupa_por_nacionalidade({
    "Mathieu BILODEAU": {
        "idade": 37,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Gabriela BITOLO": {
        "idade": 22,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Jerome BLAKE": {
        "idade": 25,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Felipe BORGES": {
        "idade": 36,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Gabriela BRAGA GUIMARAES": {
        "idade": 27,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}))