import math
def calcula_extensao(x,y):
    dx = 0
    dy = 0 
    dreal = 0
   
    for i in range(1,len(x)):
        dx += (x[i-1] - x[i])**2
        dy += (y[i-1] - y[i])**2
        dtotal = math.sqrt(dx + dy)
        dreal += dtotal

    return dreal



        
    
print(calcula_extensao([275, 290, 310, 390, 480],[75, 180, 120, 110, 150]))


                
