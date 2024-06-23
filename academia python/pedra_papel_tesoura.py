def pedra_papel_tesoura(j1 , j2 ):
  #if j1 == 'papel' or j1 == 'pedra' or j1 == 'tesoura' and j2 == 'papel' or j2 == 'pedra' or j2 == 'tesoura ': <-
     if j1 == 'pedra'and j2 == 'papel ':
        return 'dois'
     elif j1 == 'pedra' and j2 == 'tesoura':
        return 'um'
     elif j1 == 'tesoura' and j2 == 'papel':
        return 'um'
     elif j1 == 'tesoura' and j2 == 'pedra':
        return 'dois'
     elif j1 == 'papel' and j2 == 'tesoura':
        return 'dois'
     elif j1 == 'papel' and j2 == 'pedra':
        return 'um'
     elif j1 == j2 and j1 in ['pedra' ,'papel', 'tesoura'] and j2 in ['pedra' , 'papel', 'tesoura'] :
     #elif j1 == j2 :
        return 'empate'
     else :
          return 'Escolha pedra, papel ou tesoura para jogar'
    
    
    
print(pedra_papel_tesoura('w', 2))
#pq isso ta dando errado na linha inicial , pq ta passando do primeiro if ??