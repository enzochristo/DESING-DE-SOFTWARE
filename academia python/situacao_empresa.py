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


contador_normal = 0

contador_reclamacao = 0

contador_justica = 0

contador = 0

lim_reclamacoes = float(input('qual o limite de reclamacoes ? '))

lim_pedidos = float(input('qual o limite de pedidos ? '))

adicionar_pedido = input('gostaria de adicionar dados de um pedido ? ')

condicao = adicionar_pedido.upper() == 'N'

interesse = 0

percentual_reclamacao = 0

percentual_justica = 0

percentual_normal = 0

continuar = True
while continuar :
    contador += 1
    if condicao :
        continuar = False
    else:
          
        valor = float(input('qual o valor do pedido ? '))
        dias_atraso = int(input('qual a quantidade de dias em atraso ? '))
        tamanho = input('a entrega era de tamanho pequeno ou grande ? ')
        avaria = input('houve avaria ou nao ? ')
        capital = input('é para uma capital ou nao ? ')
        interesse = classifica_pedido(valor,dias_atraso,tamanho,avaria,capital)
        if interesse == 'normal' :
            contador_normal += 1

        if interesse == 'justica':
            contador_justica += 1

        if interesse == 'reclamacao' :
            contador_justica += 1

        percentual_reclamacao = (contador_reclamacao/contador) * 100

        percentual_normal = (contador_normal/contador) * 100

        percentual_justica = (contador_justica/contador) * 100

        adicionar_pedido = input('gostaria de adicionar dados de um pedido ? ')  

    
print('Pedido classificado como: ' .format(interesse))
print(f'Pedidos por classificacao: {contador_reclamacao} reclamacao, {contador_normal} normal, {contador_justica} justica')
print(f'Pedidos por classificação: {percentual_reclamacao:2f}%, {percentual_normal:.2f}%, {percentual_justica:.2f}%' )

if 0 <contador_reclamacao < 1 and 0 < contador_justica < 1:
    print('Meta atingida!')
else : 
    print('Meta nao atingida!')




#oiooio
