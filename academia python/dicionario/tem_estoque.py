def tem_estoque(dp,de):
    for key, valor in dp.items():
        if key not in de:
            return False
        else:
            if valor <= de[key]:
                resp = True
            else:
                return False
    return resp 

print(tem_estoque({
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3,
},{
    'hélice': 149,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 2,
    'turbina': 23,
}))
        


