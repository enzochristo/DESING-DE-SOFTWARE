
def quantos_uns(n):
    numero_em_str = str(n)
    contador = 0
    result = 0 
    anterior = n


    while contador + result <= len(numero_em_str)  :

        divisao  = anterior // 10
        joker = divisao*10
        
        interesse = anterior - joker
        anterior = divisao
    
        if interesse / 1 == 1 :
            result +=1
    
        else:
            contador +=1
            
    return result


print(quantos_uns(1111))

        



        
        




       

     
     
    


