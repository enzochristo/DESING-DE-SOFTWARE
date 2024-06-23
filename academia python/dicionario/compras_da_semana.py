def compras_da_semana(receitas, l_pratos):
    ingredientes = {}
    #a senha da receita é o elemento da lista de pratos
    for pratos in l_pratos:
        for ing,qtd in receitas[pratos].items():
            if ing in ingredientes:
                ingredientes[ing] += qtd
            else:
                ingredientes[ing] = qtd
    return ingredientes



#uma boa estrategia é chamar uma variavel com a senha da lista e fazer um for com essa variavel para que rode os elementos dessa lista
print(compras_da_semana({
    'Bolo de chocolate': {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    },
    'Bolinho de chuva': {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    },
    'Mingau': {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }
}, ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']
))




        