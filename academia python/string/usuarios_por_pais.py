def usuarios_por_pais(lista_emails,dominios):
    dic = {}
    for email in lista_emails:
        dominio = email[-2]+email[-1]
        usuario = email[:(email.find("@"))]
        for valor in dominios.keys():
            if valor == dominio:
                pais = dominios[valor]
            






print(usuarios_por_pais(['usuario1@insper.edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br'],{
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia'
}))
