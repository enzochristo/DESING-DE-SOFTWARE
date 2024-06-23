def aproxima_raiz(n):
    i = 0
    exp = 0
    while n >= exp:
        i += 1
        exp = i**2
    exp2 = (i-1) ** 2
    sub1 = abs(n - exp)
    sub2 = abs(n-exp2)

    if sub1 > sub2 :
        return i - 1
    else :
        return i


print(aproxima_raiz(4))




