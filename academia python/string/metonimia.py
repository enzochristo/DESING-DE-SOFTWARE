def metonimia(texto,d):
    i = 0
    texto3 = ''
    for met,nome in d.items():
        texto2 = texto.lower()
        met2 = met.lower()
        i+= 1
        if met2 in texto2:
            texto2 = texto
            texto2 = texto.replace(met,nome)
            metonimia = '_'*len(nome)
            texto = texto.replace(nome,metonimia)
            print(texto)
    for x in range(len(texto2)):
        if texto2[x] != texto[x]:
            texto3 += texto2[x].upper()
        else:
            texto3 += texto2[x]
    return texto3

print(metonimia('"Adicione uma colher de sopa de Maizena a dois copos de leite e leve ao fogo baixo, mexendo sempre. Ao final, acrescente o leite Moça."',{
'Leite Moça': 'leite condensado',
'Leite Ninho': 'leite em pó',
'Maizena': 'amido de milho',}))
        




