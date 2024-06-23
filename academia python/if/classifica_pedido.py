def classifica_pedido (valor , atraso , tamanho , avarias , destino ):
    t = str(tamanho)
    av = str(avarias)
    de = str(destino)
    
    if valor <= 1000 :
        if atraso <= 1:
          if valor <= 150 :
              if av.upper() == 'N':
                    return 'normal'
              else:
                  return 'reclamacao'
          else :
              return 'reclamacao'
        else :
            return 'reclamacao'
    else :
        if atraso <= 10 : 
            if av.upper() == 'N':
                if valor <= 10000:
                    if valor <= 5000 :
                        if de.upper() == 'N': return 'normal'
                        else : 
                            if t.upper() == 'P':
                                return 'reclamacao'
                            else : return 'normal'
                    else: return 'reclamacao'      
                else: return 'justica'
            else: return 'justica'
        else: return 'justica'
    

print(classifica_pedido(124.1,1,'p','n','S'))