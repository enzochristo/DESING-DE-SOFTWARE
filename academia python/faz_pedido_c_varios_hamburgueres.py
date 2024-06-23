def calcula_valor_liquido(valor_bruto , origem):
    if origem == 'pyfood': 
     result = .7*valor_bruto
    else :
       result = (0.985 * valor_bruto) - 7.5
    
    return result
    
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
        total *= 0.95 # se nao for maior que 33 ,                 ele nem entra no if , logo nao tera o desconto
    return total
     

origem = input('pyfood" / "whatsapp ') == 'pyfood'
valor = 0
mais_lanches = input('gostaria de adicionar um pedido ? ')== 'S'
contador = 1
if not mais_lanches and contador == 1:
    print("")
soma = 0
while mais_lanches:
 mais_lanches = input('gostaria de adicionar um pedido ? ')== 'S'
 if not mais_lanches:
     print(f'O pedido ira custar {valor}')
     break
 pao = input('qual o tipo de pao ?')
 quantidade = int(input('qual a quantiade de carnes ? '))
 salada = input('quer salada no hamburguer ? ')
 bacon = input('gostaria de bacon no hamburguer ? ')
 molho = input('gostaria de molho no seu hamburguer ? ')
 queijo = input('gostaria de queijo no seu hamburguer ? ')
 valor = print(calcula_preco_hamburguer(pao,quantidade,salada,bacon,molho,queijo))
 print(f'Valor do lanche {valor} ')
 soma += valor
 contador += 1



if contador > 1:
    valor_liquido = calcula_valor_liquido(soma,origem)
    print(f'O pedido ira custar{soma}')
    print(f'A hamburgueria ficara com {valor_liquido}')
    print('Pedido finalizado. Ate mais!')
else:
    print("")






