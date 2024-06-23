


def conversao_mi_para_km(distancia_mi):


    distancia_km = 1.6 * distancia_mi

    return distancia_km

milhas = 10 
km = conversao_mi_para_km(milhas)
"""print(f' quando a distancia em milhas for {milhas} , a distancia em km será {km}')"""

"""s1 = 'quando a distancia em milhas for ' + str(milhas) +  ' milhas , a distância em km será : '+ str(km) + ' km'

print(s1)"""

"""s2 = ' quando a distancia em milhas for de {0} milhas , a distancia em km será de {1} km '.format(milhas,km)

print(s2)"""

def positivo_e_negativo( v ):
    resultado = (-1) ** v 
    return resultado


h =  0 
w = 1
k = 2
q = -1

print(positivo_e_negativo(h))

print(positivo_e_negativo(w))

print(positivo_e_negativo(k))

print(positivo_e_negativo(q))




def soma (x , y ):
    z = x + y 
    return z 

a = input('digite o primeiro termo:  ')

b = input('digite o segundo termo:  ')

x = int(a)
y = int(b)

print((soma(x,y)))





