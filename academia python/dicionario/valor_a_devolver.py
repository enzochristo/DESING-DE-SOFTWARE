#se no caixa o preço do produto estiver menor, vale o preço do caixa. Do contrário, o cliente deve receber a diferença de volta.
def valor_a_devolver(dpl,dc,lc):
    retorno = 0
    for lista in lc:
        produto = lista[0]
        marca = lista[1]
        qtd = lista[2]
        preco_prat = dpl[produto][marca]
        preco_cx = dc[produto][marca]
        if preco_prat < preco_cx:
            retorno += qtd*(dpl[produto][marca] - dc[produto][marca])
    return retorno 


