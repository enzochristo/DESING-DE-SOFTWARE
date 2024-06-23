def transforma_base(l):
    dici = {}
    for q in l:
        sen_1dici = q['nivel']
        if sen_1dici not in dici.keys():
            dici[sen_1dici] = []
            dici[sen_1dici].append(q)
        else:
            dici[sen_1dici].append(q)
    return dici 


print(transforma_base([{'titulo': 'Em que ano faleceu Charles Babbage?', 'nivel': 'dificil', 'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'}, 'correta': 'A'}, {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?', 'nivel': 'facil', 'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Natação'}, 'correta': 'C'}, {'titulo': 'Qual destas não é uma fruta?', 'nivel': 'facil', 'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'}, 'correta': 'B'}, {'titulo': 'Qual a capital do Brasil?', 'nivel': 'facil', 'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'}, 'correta': 'A'}, {'titulo': 'Qual destas não é uma fruta?', 'nivel': 'facil', 'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'}, 'correta': 'B'}] 
  
))
    

 