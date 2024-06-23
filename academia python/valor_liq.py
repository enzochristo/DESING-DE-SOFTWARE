def calcula_valor_liquido(valor_bruto , origem):
    if origem == 'pyfood': 
     result = .7*valor_bruto
     
    else :
       result = (0.985 * valor_bruto) - 7.5
    
    return result
    
     

     
          
