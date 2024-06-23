def soma_multiplos(x,y):
    contador = 0 
    somax = 0
    somay = 0
    maior_numero = y #maior numero em relacao aos dois numeros
    menor_numero = x
    if x>maior_numero: 
        maior_numero = x
        menor_numero = y
    limite = 10 * maior_numero
    while menor_numero *contador <= limite :
        m1 = maior_numero*contador
        m2 = menor_numero*contador
        contador += 1
        if m1 % menor_numero == 0:
            m1 = 0 
        if m1 > limite :
            m1 = 0
        somax += m1
        somay += m2
        total = somax + somay
        
    return total
    
print(soma_multiplos(4,7))
       
            
           
