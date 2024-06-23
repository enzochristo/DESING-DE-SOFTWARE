def dias_de_racao(e,d):
    total = 0
    idade = d['idade']
    porte_cachorro = d['porte']
    gramas_dia= d['gramas_dia']/1000
    classificacao = ''
    if e == []:
        return 0
    if idade <= 1:
        classificacao = 'filhote'
    if 8 > idade > 1 :
        classificacao = 'adulto'
    if idade > 8:
        classificacao = 'idoso'
    for el in e:    
        porte_racao = el['porte']
        indicado = el['indicado']
        qtd = el['qtde']
        if classificacao == indicado and porte_racao == porte_cachorro:
            total += qtd
    return (total//gramas_dia)

print(dias_de_racao([
  {
      'marca': 'premier',
      'porte': 'grande',
      'indicado': 'filhote',
      'qtde': 8
  },
  {
      'marca': 'premier',
      'porte': 'grande',
      'indicado': 'adulto',
      'qtde': 5.5
  },
  {
      'marca': 'royal c.',
      'porte': 'grande',
      'indicado': 'adulto',
      'qtde': 12.0
  }
],{
  'nome': 'biribinha',
  'idade': 5.2,
  'porte': 'grande',
  'gramas_dia': 380.0
}
))


