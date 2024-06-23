def mais_frequente(l):
    d = {}
    maior = 0
    for p in l:
        if p not in d:
            d[p] = 0
        d[p] += 1
    for pa,n in d.items():
        if n > maior:
            maior = n
            palavra = pa
    return palavra

print(mais_frequente(['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']))

