def filtra_positivos(l1):
    l3 = []
    i = 0
    while i < len(l1):
        if l1[i] > 0:
            l3.append(l1[i])
        i += 1
    return l3