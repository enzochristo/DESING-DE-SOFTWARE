def calcula_media(d, country ):
    idade = 0
    qtd = 0
    for info in d.values():
        if country in info['nacionalidade']:
           idade += info['idade']
           qtd += 1 
    return idade//qtd 


print(calcula_media({
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
        "idade": 26,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}, 'Canadá'))
