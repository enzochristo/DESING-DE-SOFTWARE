numeros = int(input('digite um numero '))
l1 = []

i = 0
while numeros > 0:
    l1.append(numeros)
    numeros = int(input('digite um numero '))
  
l4 = [0] * len(l1)

while i < len(l1):
    l4[i] = l1[len(l4)-1-i]
    i += 1

print(l4)
