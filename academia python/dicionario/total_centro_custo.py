def total_centro_custo(d):
    d2 = {}
    for nomes in d.keys():
        area = d[nomes]['centro de custo']
        if area not in d2:
         area = d[nomes]['centro de custo'] 
         d2[area] = 0
        d2[area] += d[nomes]['valor']

    return d2


print(total_centro_custo({
    'Joao Silva': {
        'descricao': 'passagem para auditoria em filial',
        'centro de custo': 'tesouraria',
        'valor': 3000,
    },
    'Silvio Costa': {
        'descricao': 'alimentacao em processo de auditoria',
        'centro de custo': 'tesouraria',
        'valor': 1340.50,
    },
    'Maria Conceicao': {
        'descricao': 'inscricao em congresso internacional',
        'centro de custo': 'presidencia',
        'valor': 7200.00,
    },
    'Marcio Macedo': {
        'descricao': 'copias de memorando',
        'centro de custo': 'producao',
        'valor': 30.80,
    },
    'Marisa Monte Verde': {
        'descricao': 'curso em complaince',
        'centro de custo': 'presidencia',
        'valor': 17800.00,
    }
}))