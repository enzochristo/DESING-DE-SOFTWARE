def conta_ocorrencias(l):
    dic = {}
    for el in l:
     if el not in dic:
        dic[el]  = 0 
     dic[el] += 1
    return dic

       

print(conta_ocorrencias(['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']))