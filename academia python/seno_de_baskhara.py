import math
x = 0
sub_max = 0
continuar = True
while continuar and x < 90 :
 a = 4*x*(180-x)

 b = -x*(180-x)

 sinx_grau = a / (40500 + b )

 sinx_rad = math.radians(sinx_grau)

 sin_vdd = math.sin(math.radians(x))

 sub = abs(sin_vdd - sinx_rad)

 if sub > sub_max:
  sub_max = sub 

 elif x == 0 :
  sub_max = sub
  
 else :
  continuar = False
  print(x)
  
 x += 1
 



    

