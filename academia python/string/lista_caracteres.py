def lista_caracteres(s):
   li = []
   for l in s:
      if l not in li:
         li.append(l)
   return li
      
    
         



print(lista_caracteres('abacate'))

   