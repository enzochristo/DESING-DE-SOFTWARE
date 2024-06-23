def lojas_selecionadas(d,l):
    d2 = {}
    dinv = {}
    lista = []
    for prod in l:
        if prod not in d:
            d2[prod] = 'nao consta'
        else:
            for site,valor in d[prod].items():
                lista.append(valor)
                menor = lista[0]
                if valor < menor:
                    menor = valor
            dinv[menor] = site
            d2[prod] = dinv[menor]
            lista = []
    return d2
print(lojas_selecionadas({
    'fone de ouvido BT' : {
        'Americanas': 219.90,
        'Magazine Luiza': 209.90,
        'Amazon': 249.90      
    },
    'carregador celular USB-C': {
        'Mercado Livre': 50.00
    },
    'livro Programacao com Python': {
        'Magazine Luiza': 79.90,
        'Amazon': 59.90
    }                                           
},[
    'carregador celular USB-C',
    'livro Ciencia de Dados',
    'livro Programacao com Python'
]))
        
            






