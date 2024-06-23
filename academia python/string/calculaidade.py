def calcula_idade(idade, ano):
    id = abs(int(idade[6:]) - int(ano[6:]))-1 
    if int(ano[3:5]) >= int(idade[3:5]) :
        if int(ano[3:5]) == int(idade[3:5]):
            if int(idade[0:2]) > int(ano[0:2]):
               return id 
        return id +1
    return id
    

print(calcula_idade('15/07/2000' , '20/08/2021'))
        