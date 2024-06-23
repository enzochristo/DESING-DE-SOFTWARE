def calcula_porcentagens(dici):
    total = 0
    for valor in dici.values():
        total += valor
    for key, valour in dici.items():
        dici[key] = (valour/total)*100
    return dici 

    
print(calcula_porcentagens({
    'Erro de indentação': 493,
    'Erro de parênteses': 1102,
    'Variável inexistente': 405,
}))

