continua = True
lista_login = []
contagem = 1
while continua:
    login = input("Login: ")
    if login == "fim":
        continua = False
        break
    a = login
    while a in lista_login:
        a = login + f"{contagem}"
        contagem +=1
    lista_login.append(a)

for nome in lista_login:
    print(nome)








    


    