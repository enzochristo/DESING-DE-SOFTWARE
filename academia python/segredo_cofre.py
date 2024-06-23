
def calcula_segredo (s):
 d = s//10
 a1 = d // 10    
 a2 = d % 10 
 a3 = (s % 10 )


 if s < 100 or s > 999 :
        return -1
 if s == 0 :
        return None
 
 return a1 + a2 + a3


    

  
    
   

print(calcula_segredo(729))