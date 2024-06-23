def classifica_triangulo(a , b , c):
    if a == b == c :
        return 'equilatero'
    if a == b and not c == b :
        return 'isosceles'
    else :
        return 'escaleno'