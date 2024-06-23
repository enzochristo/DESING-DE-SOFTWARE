
def emprestimo(valor_casa , salario , anos ):
    a = anos * 12
    prestacao = valor_casa / a

    if prestacao > .3 * salario :
        return 'emprestimo nao aprovado'
    else: 
     return 'emprestimo aprovado' 
    

a = float(input('o valor da casa é : '))
b = float(input('o salario é : '))
c = float(input('o tempo que demorara em anos para pagar a casa é :'))

d = emprestimo(a,b,c)

print(f'o valor do emprestimo é {d}') #relacionei o valor da funcao com as variaveis que vao ter valores atribuidas e fiz com que o resultado seja com 3 casas decimais. 
