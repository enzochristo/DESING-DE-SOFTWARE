def pp( distancia):
 if distancia <= 200: 
        preco =  0.5 * distancia
        return preco
        
 if distancia > 200:
       preco =  ( ( distancia - 200 ) *.45)+ (200*.5)
       return preco
 
 
c = float(input('qual foi a distancia rodada ? '))
a = pp(c)

#print(f'o preco foi {pp(c): .2f}') ou pode ser feito assim :
print(f'o preco foi de {pp(c): .2f}')

      
