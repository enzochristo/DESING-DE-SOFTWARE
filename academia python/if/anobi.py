def eh_bissexto(ano):
    if ano % 4 == 0 :
        if ano % 100 == 0 and  ano % 400 == 0 : 
            return True
        else :
           if ano % 100 == 0 :
                return False
           return True
    return False        
            



       

    
  
     






#Se o ano não for múltiplo de 4, ele não é bissexto;
"""Se o ano for múltiplo de 4 e de 400, ele é bissexto;
Se o ano for múltiplo de 4 e de 100, mas não de 400, ele não é bissexto;
Caso contrário, ele é bissexto """

    