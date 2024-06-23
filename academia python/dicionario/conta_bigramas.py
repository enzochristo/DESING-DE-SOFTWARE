def conta_bigramas(p):
    d ={}
    for i in range(1,len(p)):
        l1 = p[i-1]
        l2 = p[i]
        bi = l1+l2
        if bi not in d:
            d[bi] = 0
        d[bi] += 1
    return d

print(conta_bigramas('banana nanica'))
