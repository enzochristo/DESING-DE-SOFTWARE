def interseccao_chaves(d1,d2):
    l = []
    k1 = d1.keys()
    k2 = d2.keys()
    for i in k1:
        if i in k2:
            l.append(i)
    return l
 
        
    return l


  
print(interseccao_chaves({'A':1,'B':2,'C':3},{'A':3, 'B':4, 'C': 6, 'E': 9, 'Q': 4}))