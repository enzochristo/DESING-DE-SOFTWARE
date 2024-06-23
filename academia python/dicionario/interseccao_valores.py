def interseccao_valores(d1,d2):
    v1 = d1.values()
    v2 = d2.values()
    # tanto em values quanto em keys, é criado uma lista com os valores ou com as chaves do dicionario, entao basta percorred os elementos dessa lista e ver se ta na outra lista
    l = []
    for el in v1 :
        if el in v2:
            l.append(el)
    return l