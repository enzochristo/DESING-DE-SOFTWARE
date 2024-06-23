def junta_listas(listas):
    junta = []
    for el in range(len(listas)):
        for integrantes in range(len(listas[el])):
            junta.append(listas[el][integrantes])
    return junta


print(junta_listas([[1,2,3],[4,5,6],[7,8],[9],[10]]))