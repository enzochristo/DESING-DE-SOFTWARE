import random
def sorteia_pais(d):
    lista = []
    for pais in d:
        lista.append(pais)
    pais_aleat = random.choice(lista)
    return pais_aleat

print(sorteia_pais({
    'afeganistao': {'area': 652230, 'populacao': 31390200, 'capital': 'Cabul'},
    'arabia saudita': {'area': 2149690, 'populacao': 34268528, 'capital': 'Riade'},
    'armenia': {'area': 29743, 'populacao': 2957731, 'capital': 'Erevan'},
    'azerbaijao': {'area': 86600, 'populacao': 10023318, 'capital': 'Baku'},
    'bahrein': {'area': 765, 'populacao': 1501635, 'capital': 'Manama'},
    'bangladesh': {'area': 147570, 'populacao': 167310838, 'capital': 'Daca'},
    'brunei': {'area': 5765, 'populacao': 433285, 'capital': 'Bandar Seri Begawan'},
    'butao': {'area': 38394, 'populacao': 763092, 'capital': 'Thimbu'}
}))


