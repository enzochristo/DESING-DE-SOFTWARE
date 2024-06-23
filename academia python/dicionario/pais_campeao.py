def pais_campeao(d):
    max_ouro = -1
    campeao_ouro = []
    for pais, medalhas in d.items():
        if medalhas['ouro'] > max_ouro:
            max_ouro = medalhas['ouro']
            campeao_ouro = [pais]
        elif medalhas['ouro'] == max_ouro:
            campeao_ouro.append(pais)
    if len(campeao_ouro) == 1:
        return campeao_ouro[0]
    max_prata = -1
    campeao_prata = []
    for pais in campeao_ouro:
        if d[pais]['prata'] > max_prata:
            max_prata = d[pais]['prata']
            campeao_prata = [pais]
        elif d[pais]['prata'] == max_prata:
            campeao_prata.append(pais)
    if len(campeao_prata) == 1:
        return campeao_prata[0]
    max_bronze = -1
    campeao_bronze = ''
    for pais in campeao_prata:
        if d[pais]['bronze'] > max_bronze:
            max_bronze = d[pais]['bronze']
            campeao_bronze = pais
    return campeao_bronze
    
            




    

        
        

        

print(pais_campeao({
    'China': {
        'ouro': 20,
        'prata': 35,
        'bronze': 40 
    },
    'Canadá': {
        'ouro': 5,
        'prata': 15,
        'bronze': 20
    },
    'Estados Unidos': {
        'ouro': 25,
        'prata': 30,
        'bronze': 40
    },
    'Brasil': {
        'ouro': 10,
        'prata': 10,
        'bronze': 8
    }
}))


        
    