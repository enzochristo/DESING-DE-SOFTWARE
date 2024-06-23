def humor(l):
    compra = 0
    venda = 0

    for el in range(len(l)):
        for i in range(len(l[el])):
            if  l[el][i]== 'comprar':
                compra += 1
            if l[el][i] == 'vender':
                venda += 1
        del(l[el])
        if venda > compra:
            l.insert(el,'vender')
        if venda == compra:
            l.insert(el,'empate')
        if compra > venda:
            l.insert(el,'comprar')
        compra = 0
        venda = 0
    return l

print(humor([
    ['vender', 'comprar', 'vender','comprar'],
    ['comprar', 'comprar', 'vender','comprar'],
    ['comprar', 'vender','vender', 'vender', 'vender' ],
    ['vender', 'comprar', 'vender', 'vender']
]))


