def contabiliza_combustivel(log):
    d2 = {}
    d3 = {}
    for dici in log.values():
        combust = dici['tipo']
        custo = dici['custo']
        litros = dici['litros']
        if combust not in d2:
            d2[combust] = {'custo total':0, 'total litros': 0 }
        #custo2 = d2[combust]['custo total']
        #litros2 = d2[combust]['total litros']
        d2[combust]['custo total'] += custo #+ custo2
        d2[combust]['total litros'] += litros #+ litros2
    for combustivel in d2.keys():
        d3[combustivel] = {'total litros':d2[combustivel]['total litros'] , 'custo por litro':d2[combustivel]['custo total']/d2[combustivel]['total litros'] }
        #custo_total_comb = d2[combustivel]['custo total']
        #litro_total_comb = d2[combustivel]['total litros']
        #d3[combustivel]['total litros'] = litro_total_comb
        #d3[combustivel]['custo por litro'] = custo_total_comb/litro_total_comb"""
    return d3 
        

         
    return d2
print(contabiliza_combustivel({
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}))
    





