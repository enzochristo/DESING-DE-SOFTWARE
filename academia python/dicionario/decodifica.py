def decodifica(codificada, sistema):
    dinv = {}
    for k, v in sistema.items():
        dinv[v] = k
    original = ''
    for i in codificada:
        if i in dinv:
            letra = dinv[i]
            original += letra
        else:
            original += i
    return original
        
print(decodifica('*b*c*t&',{'a': '*', 'e': '&'}))
'*b*c*t&'
{'a': '*', 'e': '&'}