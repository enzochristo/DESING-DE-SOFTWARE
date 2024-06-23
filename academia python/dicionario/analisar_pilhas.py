def analisar_pilhas(d,lp):
    classificacao = []
    for nomes,d2 in d.items():
            modelo =''.join(list(d[nomes].keys()))
            for i in range(len(lp)):
                if lp[i][0] != nomes or lp[i][1]!= modelo:
                    classificacao.append('E')
                else:
                    if nomes == lp[i][0]:
                        tensao = d2[modelo]['volts']
                        limite = d2[modelo]['limite']
                        recharge = d2[modelo]['recarregavel']

                        estado_max = tensao *(1-limite)
                        if estado_max <= lp[i][2]:
                            classificacao.append('N')
                        else:
                         if recharge:
                                classificacao.append('R')   
                         elif not recharge:
                                classificacao.append('D')   
    return classificacao


print(analisar_pilhas({
  "duracell": {
    "alcalina": {
      "capacidade": "2700 mah",
      "volts": 1.5,
      "limite": 0.1,
      "recarregavel": False
    }
  },
  "panasonic": {
    "eneloop": {
      "capacidade": "2700 mah",
      "volts": 1.2,
      "limite": 0.1,
      "recarregavel": True
    },
    "eneloop pro": {
      "capacidade": "3200 mah",
      "volts": 1.2,
      "limite": 0.12,
      "recarregavel": True
    }
  }
},[
  ['duracell', 'alcalina', 1.17],
  ['duracell', 'alcalina', 1.57],
  ['panasonic', 'eneloop pro', 1.21],
  ['panasonic', 'eneloop pro', 1.01],
  ['panasonic', 'eneloop pro', 1.23],
  ['panasonic', 'eneloop', 1.06],
  ['panasonic', 'eneloop', 1.15],
  ['panasonic', 'eneloop', 1.28],
]))



