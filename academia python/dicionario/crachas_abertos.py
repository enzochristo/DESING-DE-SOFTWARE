def crachas_abertos(log):
    d2 = {}
    lista2 = []
    e = 0
    s = 0
    for valores in log.values():
         for tempo in valores.keys():
            lista = valores[tempo]
            cracha = lista[0]
            retorno = lista[1]
            if cracha not in d2:
             d2[cracha] = {'entrada':0, 'saida':0}
            if retorno == 'E':
               d2[cracha]['entrada'] += 1
            else:
               d2[cracha]['saida'] += 1
    for cra in d2:
       if d2[cra]['entrada'] != d2[cra]['saida']:
          lista2.append(cra)
    return lista2
            
    
        
print(crachas_abertos({
    'catraca 1': {
        '04h10m06s': ['cracha F', 'E'],
        '07h07m34s': ['cracha F', 'S'],
        '08h59m15s': ['cracha Y', 'S'],
        '15h49m41s': ['cracha Y', 'S'],
        '16h54m01s': ['cracha X', 'E'],
        '21h47m12s': ['cracha F', 'E'],
        '22h36m08s': ['cracha A', 'E']
    },
    'catraca 2': {
        '07h43m52s': ['cracha X', 'E'],
        '16h49m39s': ['cracha Y', 'E'],
        '17h56m02s': ['cracha X', 'S'],
        '23h11m16s': ['cracha X', 'S']
    },
    'catraca 3': {
        '01h07m58s': ['cracha Y', 'E'],
        '07h25m10s': ['cracha F', 'S'],
        '23h23m17s': ['cracha X', 'S']
    }
}))