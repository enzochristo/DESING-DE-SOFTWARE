import math

def calcula_euler(x,n):
 fatorial = 1
 soma = 0
 contador = 0
 while  contador != n :
        soma = soma + (x ** contador)/fatorial 
        contador += 1
        fatorial = fatorial * contador 
  #soma = soma + (x ** contador)/fatorial 
 return soma

print(calcula_euler(2,10))