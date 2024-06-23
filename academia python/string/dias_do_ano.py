def dias_do_ano(data):
    i = 0
    soma = 0
    d_meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    ano = data[-4:]
    d0 = f"01/01/{ano}"
    mes_ref = d0[3:5]
    if int(data[0])==0:
        dia = int(data[1])
    else:
        dia = int(data[:2])
    if int(data[3]) == 0:
        mes = int(data[4])
    else:
        mes = int(data[3:5])

    while i < mes:
        i+=1
        if mes == i:
         soma = soma + abs(dia-int(d0[1])) 
         return soma
        else:
            soma += d_meses[i]
    return soma - int(d0[1])

print(dias_do_ano('16/05/2021'))
    

    
    