import math 
def quantia_de_raizes(a ,b , c):
    delta = (b)**2 - ( 4 * a * c )
    if delta > 0 :
        x1 = (-(b) + math.sqrt(delta))/(2*a)
        x2 = (-(b) + math.sqrt(delta))/(2*a)
        return x1,x2,2
    if delta == 0 :
       x1= -(b) /(2*a)
       return 1
    
    if delta < 0 :
        return 0 
    
    
print(quantia_de_raizes(-3 , 0 , 0))