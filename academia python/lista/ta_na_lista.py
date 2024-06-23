def esta_na_lista(pais,lista):
    i = 0
    while i < len(lista):
        lista2 = lista[i]
        i += 1
        if pais == lista2[0]: 
            return True
    return False


            

print(esta_na_lista('siria', [['libia',3678],['franca',3998],['egito',5008],['india',9919],['japao',13896]]))
