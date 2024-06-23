import math
contador = 1
continuar = True
def calcula_pi(n):
    pi = math.sqrt(6/(contador**2))
    while contador <= n  :
     contador +=1
     pi = math.sqrt(6/(contador**2))
     return pi
