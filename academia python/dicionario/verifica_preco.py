def verifica_preco(nome, dic_nome,dic_cor):
    for key in dic_nome.keys():
        if key == nome:
         cor =  dic_nome[key]
         for key2 in dic_cor.keys():
            if key2 == cor:
               result = dic_cor[key2]
               return result
               
            

print(verifica_preco("Pinóquio",{"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"},{"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
))


