def verifica_progressao(lista):
    pa = 1
    pg = 1
    q = 0
    for el in range(1,len(lista)):
        r = lista[-1] - lista[-2] 
        if lista[0]!=0:
            q = lista[1]/lista[0]
            if lista[el]/lista[el-1] == q:
                pg += 1
        if lista[el] - lista[el-1] == r:
            pa += 1 
    if (q == 0 or q ==1) and r == 0  :
        return 'AG'
    if pg  == len(lista):
        return 'PG'
    if pa == len(lista):
        return 'PA'
    else:
        return 'NA'


print(verifica_progressao([100,100,100,100,100]))
    