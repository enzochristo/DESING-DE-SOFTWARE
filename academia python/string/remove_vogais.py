def remove_vogais(txt):
    vogais = ['a','e','i','o', 'u']
    txt2 = ''
    for l in txt:
        if l.lower() not in vogais:
            txt2 += l
    return txt2
            

print(remove_vogais('DESOFT'))

