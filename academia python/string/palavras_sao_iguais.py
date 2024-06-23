def palavras_sao_iguais(s):
    if '-' in s:
        split = s.split('-')
        if split[0] == split[1]:
            return True
    return False
print(palavras_sao_iguais('abobrinha'))