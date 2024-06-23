def nivel_idh(idh):
    if idh >= .8 and idh <= 1.0 : 
     return 'Muito Alto '
    elif idh >= 0.7 and idh < 0.8:
       return 'Alto'
    elif idh >= .555 and idh <  .7:
       return 'medio'
    elif idh >= .35 and idh < .555:
       return 'Baixo'
    else : 
       return 'sem dados'
    
  
a = float(input('qual o nivel de idh ? '))
print(f'o nivel de idh é : {nivel_idh(a)}' )
