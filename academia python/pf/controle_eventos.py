def controle_eventos(dtrabalhado):
    d = {}
    for eventos in dtrabalhado.values():
        for evento in eventos:
            if evento not in d:
                d[evento] = {'total':0,'média mensal':0}
            d[evento]['total'] += len(eventos[evento])
    for evento in d:
        d[evento]['média mensal'] = d[evento]['total']/len(dtrabalhado)

    return d
print(controle_eventos({
    'janeiro': {
                'casamento'  : [10,24,25],
                'aniversário': [2,7] 
            },
    'julho'  : {
                'casamento': [7],
                'bodas'    : [3,11]
            },
    'abril'  : {
                'casamento' : [10],
                'lancamento': [13,17,29]
                },
    'fevereiro': {
                'aniversário': [7,14,21,28],
                'bodas'      : [10,24,25]
                }  
}))


