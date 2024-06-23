import math 

def will_it_float(P , R , r):
   d_agua = 997
   volume = math.pi**2 * 2 * R * r * math.pow(10,-6)
   massa = P
   densidade = massa / volume
   if densidade > d_agua :
    return False
   else: 
     return True
    

 
a = float(input('o peso é :  '))
b = float (input('o raio maior é : '))
c = float(input('raio menor é : '))

print(will_it_float(a,b,c))

