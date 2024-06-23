def eh_bissexto(ano):
    if ano % 4 == 0 :
        if ano % 100 == 0 and  ano % 400 == 0 : 
            return True
        else :
           if ano % 100 == 0 :
                return False
           return True
    return False   

def valida_data(dia , mes , ano):
   if dia < 1 or dia > 31 : return False
   if mes < 1 or mes > 12 : return False
   if mes in [2 , 4 ,6 ,9 , 11] and dia >= 31: return False
   if mes ==2 : 
       if dia == 30: return False
       if dia == 29 and not eh_bissexto(ano): return False
   return True
   
 


