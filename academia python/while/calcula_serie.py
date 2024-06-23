def calcula_serie(a,b,n):
    contador = -1
    limite = n 
    soma = 0 
    while contador + 1 != limite :  
     contador +=1
     baixo = a**(contador*b)
     i = 1/baixo
     soma += i
    return soma

print(calcula_serie(2,1,1))



    

