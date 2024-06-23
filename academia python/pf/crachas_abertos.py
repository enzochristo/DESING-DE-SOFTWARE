def limpa_nomes(nome):
    nome = (nome).split()
    n = ''
    for i in range(len(nome)):
        if i == len(nome) -1:
            n +=' ' + nome[i]
        else:
            n += ' '+ nome[i][0]
    return n.strip()


def crachas_abertos(listas):
    d = {}
    d2 = {}
    for lista in listas:
        nome = limpa_nomes(lista[1])
        hora = lista[0]
        print(hora)
        evento = lista[2]
        if nome not in d:
            d[nome] = {'qtd':0,'E':[],'S':[]}
        if evento == 'E':
            d[nome]['qtd'] += 1
            if d[nome]['qtd'] > 1:
                d[nome]['E'].append(hora)
        else:
            d[nome]['qtd'] -= 1
            if d[nome]['qtd'] < 0:
                d[nome][evento].append(hora)
    for nome,lista in d.items():
        qtd = d[nome]['qtd']
        if qtd != 0:
            if qtd > 0:
                d2[nome] = d[nome]['E'][0]
            else:
                d2[nome] = d[nome]['S'][0]
    return d2


    
        


print(crachas_abertos([
    ['07h01m58s', 'Sara Monteiro Santos', 'E'],
    ['07h03m52s', 'André Castro', 'E'],
    ['07h04m01s', 'André Castro', 'S'],
    ['07h05m06s', 'Ana Rezende Souza Souza', 'E'],
    ['07h07m34s', 'Ana Rezende Souza Souza', 'S'],
    ['07h09m15s', 'Sara Monteiro Santos', 'S'],
    ['07h16m02s', 'André Castro', 'E'],
    ['07h19m16s', 'André Castro', 'E'],
    ['07h25m10s', 'Ana Rezende Souza Souza', 'S'],
    ['07h29m39s', 'Sara Monteiro Santos', 'E'],
    ['07h36m08s', 'Pedro Paulo Farias', 'S'],
    ['07h39m41s', 'Sara Monteiro Santos', 'S'],
    ['07h47m12s', 'Ana Rezende Souza Souza', 'E'],
    ['07h56m17s', 'André Castro', 'S'],
    ['08h06m23s', 'André Castro', 'E'],
    ['08h22m10s', 'Ana Rezende Souza Souza', 'S'],
    ['08h56m17s', 'André Castro', 'S']
]
))