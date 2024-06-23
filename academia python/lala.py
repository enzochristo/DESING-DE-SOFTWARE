numero = int( input('quantos cigarros sao fumados diariamente ? '))

anos = int(input ('a quantos anos ja se tem o habito de fumar ? '))

def tempo_de_vida(numero, anos ):
    anos_em_dias = anos * 365
    dano = 10/1440
    resultado =  numero * dano * anos_em_dias
    return resultado

#numero = int( input('quantos cigarros sao fumados diariamente ? '))

#anos = int(input ('a quantos anos ja se tem o habito de fumar ? '))

print(tempo_de_vida(numero,anos))
