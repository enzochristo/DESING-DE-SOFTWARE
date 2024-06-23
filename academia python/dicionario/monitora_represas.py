def monitora_represas(dinicio,dvariacao):
    d = {}
    lista = []
    val_liq = 0
    for rep,info in dvariacao.items():
        for dias in info.keys():
            val_liq += (info[dias][0] - info[dias][1])
            capacidade = dinicio[rep]['capacidade']
            qtd = (dinicio[rep]['volume']/100) * capacidade
        reservatorio = ((val_liq + qtd)/capacidade)* 100
        val_liq = 0
        if reservatorio < 20:
            if 'emergencia' not in d:
                d['emergencia'] = []
            lista = d['emergencia']
            lista.append(rep)
            d['emergencia'] = lista
            lista = []
            reservatorio = 0
        elif reservatorio < 50 :
            if 'critico' not in d:
                d['critico'] = []
            lista = d['critico']
            lista.append(rep)
            d['critico'] = lista
            lista = []
            reservatorio = 0
        elif reservatorio < 70:
            if 'atencao' not in d:
                d['atencao'] = []
            lista = d['atencao']
            lista.append(rep)
            d['atencao'] = lista
            lista = []
            reservatorio = 0
        elif reservatorio <= 100:
            if 'normal' not in d:
                d['normal'] = []
            lista = d['normal']
            lista.append(rep)
            d['normal'] = lista
            lista = []
            reservatorio = 0
        elif reservatorio > 100:
            if 'escoar' not in d:
                d['escoar'] = []
            lista = d['escoar']
            lista.append(rep)
            d['escoar'] = lista
            lista = []
            reservatorio = 0
    return d

print(monitora_represas({
    'cantareira': {
        'capacidade': 982000,
        'volume': 25
    },
    'guarapiranga': {
        'capacidade': 171000,
        'volume': 95
    },
    'alto tiete': {
        'capacidade': 540000,
        'volume': 55
    }
},{
    'cantareira': {
        '01': [5000,30000],
        '02': [10000,35000],
        '03': [0,29000],
        '04': [31000,28000],
        '05': [0,29000]
    },
    'guarapiranga': {
        '01': [6000,10000],
        '02': [38000,12000],
        '03': [35000,14000],
        '04': [0,13000],
        '05': [15000,12000]
    },
    'alto tiete': {
        '01': [18000,30000],
        '02': [15000,25000],
        '03': [17700,24000],
        '04': [41000,28000],
        '05': [13000,24000]
    }
}))








    


        



