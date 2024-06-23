#Faça uma função que recebe 
#o investimento inicial, o número de meses investidos e o nome do ativo

#retornar o valor total do investimento no ativo escolhido 
#com o devido rendimento e bônus aplicado, se for o caso.

def calcula_investimento(inv_0,meses,nome):
    i = 1
    interesse = 0
    bonus = 0
    soma = inv_0

    while i <= meses:
        if nome == 'CDB':
            interesse = 1.3/100 * soma
            soma += interesse
            if i % 6 == 0 :
               soma = (1+ (1.2/100)) * soma
               
    
        elif nome =='LCA':
            interesse = 1.45/100 * soma   
            soma += interesse
            if i % 4 == 0 :
                soma = (1+ 1/100) * soma
                      
        else :
            interesse = 1.6/100 * soma
            soma += interesse
        i+= 1
    return soma

print(calcula_investimento(1000,12,'CDB'))


