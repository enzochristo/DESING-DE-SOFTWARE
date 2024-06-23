def preco_medio(l):
    d = {}
    soma = 0
    for linfo in l:
        acao = linfo[0]
        preco = linfo[2]
        if acao not in d:
            d[acao] = []
        d[acao].append(preco)
    for acao,lista in d.items():
        tam = len(lista)
        for preco in lista:
            soma+= preco
        d[acao] = soma/tam
        soma= 0 
    return d

print(preco_medio([
	['BBAS3', '11:09:05', 51.32],
	['USIM5', '15:25:42', 16.77],
	['USIM5', '16:00:08', 11.84],
	['BBAS3', '16:12:46', 55.59],
	['SLCE3', '16:13:39', 37.74]
]))

        
        