preco_p = 0
acres = 0
if input('p1 ') == 'P' :
 preco_p = 50
elif input('p1 ') == 'M':
    preco_p = 70
elif input('p1 ') == 'G':
    preco_p = 90

if input('p2') == 'S':
    acres = 1.15 * preco_p

if input('p3 ') == 'S':
    acres = acres + preco_p * 1.1

if input('p4 ') == 'S':
    acres += 12
 
if input('p5 ') == 'S':
    acres = acres + 20
    if preco_p == 90 :
        acres= preco_p * .93

preco = preco_p + acres

print(preco)