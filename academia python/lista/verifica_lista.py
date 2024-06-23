def verifica_lista(l1):
    i = 0 
    resposta = 'misturado'
    if len(l1) == 0 :
            return 'misturado'
    while i < len(l1):
        if len(l1) >= 2:
            if (l1[i-1] % 2 == 0 and l1[i] % 2 != 0 ) or (l1[i-1] % 2 != 0 and l1[i] % 2 == 0 ):
                return 'misturado'
            elif l1[i] % 2 == 0 and l1[i-1] % 2 == 0:
                resposta = 'par'
            else:
                resposta = 'impar'

        if len(l1) ==  1: 
             if  l1[i] % 2 == 0: 
                return 'par'

             if l1[i] % 2 != 0:
                return 'impar' 
    
            

        
        i += 1
    return resposta


print(verifica_lista([]))