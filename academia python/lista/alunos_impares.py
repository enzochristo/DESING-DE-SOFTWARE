def alunos_impares(lista):
    i = 1
    lista_result = []
    while i < len(lista) :
        lista_result.append(lista[i])
        i += 2
    return lista_result