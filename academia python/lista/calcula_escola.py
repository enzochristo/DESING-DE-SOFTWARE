def calcula_escola(l):
    soma = 0
    for i in range(len(l)):
        w = 0
        min = l[i][w]
        for el in range(len(l[i])):
            if min > l[i][el]:
                min = l[i][el]
                w = el
        del(l[i][w])
    for x in range(len(l)):
        for y in range(len(l[0])):
            soma += l[x][y]
    return soma

    


                       
            

    

        

            
   


print(calcula_escola([[9.7, 9.9, 9.7, 9.8], [9.7, 9.9, 9.7, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.4, 9.6, 9.8, 10], [9.9, 10, 9.9, 9.9], [0, 9.8, 9.8, 9.8], [10, 9.8, 10, 10]]

))



        

