def detectar_acao(dic,stop):
    resp = ''
    infinitivo = ['ar','er','ir','or']
    dr = {}
    l = []
    for pessoas, dhorarios in dic.items():
        dr[pessoas] = ''
        for mensagem in dhorarios.values():
            lmensagem = mensagem.split()
            linteresse = []
            for palavra in lmensagem:
                if palavra not in stop:
                    linteresse.append(palavra)               
            for i in range(len(linteresse)):
                if linteresse[i][-2:] in infinitivo:
                    if i != len(linteresse) -1:
                        resp = linteresse[i] + ' ' + linteresse[i+1]
                    else:
                        resp = linteresse[i]
                    l.append(resp)
        dr[pessoas] = l 
        l = []
    return dr
# resumo do codigo: para ter a virgula com strings, é necessario somar elas e é importante resetar a lista apos inserir ela no dicionario 

print(detectar_acao({
    'zezin1': {
        '2020-11-05 08:15:30' : 'produto ruim vou processar já vocês',
        '2020-11-05 08:16:01' : 'é um absurdo',
        '2020-11-05 08:18:09' : 'pode enviar no meu email por favor?',
    },
    'mariarita': {
        '2020-10-01 05:05:00' : 'gostaria de comprar um sofá',
        '2020-10-01 05:05:09' : 'quais formas de pagamento aceitam?',
        '2020-10-01 05:08:39' : 'conseguem entregar na minha moradia',
        '2020-10-01 06:01:03' : 'mesmo que seja em uma chácara?',
    },
    'juca123': {
        '2021-02-09 05:05:00' : 'perdi o boleto de pagamento',
        '2021-02-09 05:05:09' : 'e ainda nao sei usar pix',
        '2021-02-09 05:08:39' : 'poderiam emitir o boleto novamente',
        '2020-02-09 06:01:03' : 'e mandar pro meu email',
    }
},
[
    'vou', 'meu', 'minha', 'o', 'pro',
    'para', 'já', 'é', 'no', 'na',
    'uma', 'por', 'um', 'e', 'em'
]))
            
            
            