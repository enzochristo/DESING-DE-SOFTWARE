palavra = input('palavra: ') 
lista = []
continuar = True
contador = 0
while continuar:
    primeira_letra = palavra[0]
    if primeira_letra == 'a':
        lista.append(palavra)
    elif palavra == 'fim': break
    palavra = input('palavra: ') 

while contador < len(lista):
    print(lista[contador])
    contador += 1

        


