def extrai_nomes_de_usuarios(emails):
 lista = []
 for email in emails:
        lista.append(email[:email.find('@')])
 return lista





