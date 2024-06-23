def define_vencedores(l_sorteados,dp):
  l_acertos = []
  d_contagem = {}
  max = 0
  for nome,lista in dp.items():
        for num in lista:  
            if nome not in d_contagem:
                d_contagem[nome] = 0
            if num in l_sorteados:
                d_contagem[nome] += 1
  max = d_contagem[nome] 
  for qtd in d_contagem.values():
    if qtd > max:
        max = qtd
  for nome,acertos in d_contagem.items():
      if acertos >= max:
          l_acertos.append(nome)
  return l_acertos
  
        


print(define_vencedores([2, 3, 9, 11, 14, 15, 16, 17, 18, 19],{
    'joao': [3, 5, 7, 8, 18],
    'maria': [1, 5, 6, 11, 19]
}
))
      

    
       
    

         

 





        






            


    
        