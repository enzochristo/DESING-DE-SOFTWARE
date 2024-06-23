def calcula_preco_hamburguer( pao , carne , salada , bacon , molho , queijo ) :
    
    if pao == 'brioche' :
        preco_pao = 7.00

    elif pao == 'australiano' :
        preco_pao = 5.25

    if carne >= 1 : 
        preco_carne = 8.00 + ((carne - 1) * 5.00 )
    else:
        preco_carne = 0

    if salada == 'S':
        preco_salada = 3.00
      
    else:
        preco_salada = 0.0
        
    if bacon == 'S' : 
        preco_bacon = 7.5
        
    else :
        preco_bacon = 0
        
    if molho == 'S' :
        preco_molho = 1.00
        
    else:
        preco_molho = 0
       
    if queijo == 'S' : 
        preco_queijo = 5.40
   
    else:
        preco_queijo = 0
    
    total = preco_carne + preco_pao + preco_salada + preco_molho + preco_queijo + preco_bacon
    if total > 33 :
        total *= 0.95   # se nao for maior que 33 ,ele nem entra no if , logo nao tera o desconto
    return total
      



    
