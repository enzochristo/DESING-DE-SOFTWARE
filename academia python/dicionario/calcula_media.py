def calcula_media(l):
    soma = 0
    i = 0
    for el in l:
        for valor in el.values():
            i+=1
            soma += valor
    soma = soma/i
    
    return soma

print(calcula_media([ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]))
