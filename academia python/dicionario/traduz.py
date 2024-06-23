def traduz(l,dic):
    l1 = []
    for key in l:
        l1.append(dic[key])
    return l1
print(traduz(['blackberry', 'cherry', 'plum', 'apple', 'pineapple'] ,{'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'} ))




