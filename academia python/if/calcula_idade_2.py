def calcula_idade (dia_n , mes_n , ano_n , dia , mes , ano):
    idade = ano - ano_n
    if mes == mes_n and dia >= dia_n:
        return idade
    elif mes > mes_n:
        return idade
    else :
        return idade - 1
    
     

a = int(input('dia niver'))
b = int(input ('mes niver'))        
c = int(input('ano niver'))

d = int(input('dia'))
e = int(input('mes'))
f = int(input('ano'))

print(calcula_idade(a,b,c,d,e,f))
