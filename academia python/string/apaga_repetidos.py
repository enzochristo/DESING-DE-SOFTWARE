def apaga_repetidos(s):
    s= s.lower()
    li = []
    for l in range(len(s)):
        if s[l] not in li:
            li.append(s[l])
        else:
            s =  s.replace(s[l], '*')
    return s

print(apaga_repetidos('banana'))


        