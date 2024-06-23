def classifica_idade (idade) : 
         if idade < 0 or idade > 150 :
           return 'um mutante '
         elif idade <= 11 :
               return 'crianca'
         elif idade > 11 and idade < 17 :
             return 'adolescente'
         elif idade > 18 and idade < 60 :
               return 'adulto'
         else : 
              return 'idoso'
             
         
         


a = int(input('qual a sua idade ? '))

print(f'a partir da idade concluimos que voce é um(a) : {classifica_idade(a)}' )


