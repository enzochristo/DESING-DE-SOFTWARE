import math 
#sempre que for programa , tem que ter um input ? 
v = float(input('velocidade da jaca '))
teta = float(input('angulo de inclinacao :'))
g = 9.8
alvo = 100
teta_radians = math.radians(teta)
raio_esp = 2 
d = v**2 * math.sin(2*teta_radians)/g 
b = abs( alvo - d )<= raio_esp

if b :
    a = 'Acertou!'
if d < alvo and not b: 
    a = 'Muito perto'
if d > alvo and not b: 
    a = 'Muito longe'

print(a)



