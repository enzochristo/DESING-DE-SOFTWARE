def junta_nome_sobrenome(nome,sobrenome):
    i = 0
    nome_completo = []
    full_name = []
    while i < len(nome):
        full_name = str(nome[i]) + "" + str(sobrenome[i])
        nome_completo.append(full_name)
        i += 1
    return nome_completo