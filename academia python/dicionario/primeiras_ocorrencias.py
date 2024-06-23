def primeiras_ocorrencias(palavra):
    dic = {}
    i = -1
    for el in palavra:
        i += 1
        if el in dic:
            dic[el] += 0
        else:
         dic[el] = i

    return dic

print(primeiras_ocorrencias('abracadabra'))
