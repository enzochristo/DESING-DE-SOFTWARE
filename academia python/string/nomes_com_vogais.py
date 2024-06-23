def nomes_com_vogais(ln):
    lista_vogais = ['A','E','I','O','U']
    resp = []
    vogal = 0
    cons = 0
    for nome in ln:
        if nome[0:1].upper() in lista_vogais:
            vogal += 1
        else:
            cons+=1
    resp.append(vogal)
    resp.append(cons)
    
    return resp

print(nomes_com_vogais(["André", "Carlos", "João", "Otavio", "Thiago"]))
        