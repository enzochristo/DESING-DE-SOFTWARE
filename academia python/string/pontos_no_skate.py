
def limpa_frase(texto):
    proibidos = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[']
    p = ' '
    for palavras in texto.lower():
        if palavras not in proibidos:
            p += palavras
    return p


def limpa_manobras(manobras):
    dici = {}
    for manobra in manobras.keys():
        pontuacao = manobras[manobra]
        manobra = manobra.lower()
        lista = pontuacao.split()
        dici[manobra] = int(lista[0])
    print(dici)
    return dici


def pontos_no_skate(dmanobras,dperformances):
    d = {}
    manobras = limpa_manobras(dmanobras)

    for sktista in dperformances.keys():
        d[sktista] = {"qtde manobras":0,"total pontos":0}
        frases = dperformances[sktista]['frases']
        for frase in frases:
            frase = limpa_frase(frase)
            frase = frase.split()
            print(frase)
            for palavra in frase:
                if palavra in manobras:
                    d[sktista]["qtde manobras"] +=1
                    d[sktista]["total pontos"] += manobras[palavra]
    return d

manobras = {'ollie': '1 ponto', 'nollie': '01 ponto', 'heelFLIP': '02 pontos', 'varialflip': '5 pontos', 'casperflip': '07 pontos', 'IMPOSSIBLE': '019 pontos'} 
performances = {'Tony Hawk': {'narrador': 'galvão bueno', 'frases': ['Bem amigos da rrrrede globo', 'vem aí Tony Hawk', 'Ele manda um Ollie, agora um Nollie,', 'haaaaja coração,vai com tuUuUUuudo Tony Hawk']}, 'Fadinha': {'narrador': 'Karen Jonz', 'frases': ['vem logo de Varialflip', 'um Casperflip, outro varialflip', 'UM NOLLIE, OUTRO CASPTERflip', 'olha aí, mandou um Impossible.', 'Mano, ficou parecendo', 'um peixe morto ali de propósito', 'pra matar todo mundo do coração', 'aí depois, era pegadinha']}, 'Guilherme da Academia': {'narrador': 'jô soares', 'frases': ['Hoje a noite teremos uma performance', 'de um skatista muito especialo Guilherme da Academia.', 'Lá vem ele... xiii... caiu!!!', 'skate não é a especialidade dele.', 'Bira, o que você achou disso?']}}

print(pontos_no_skate(manobras,performances))