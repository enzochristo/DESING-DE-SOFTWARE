def notas_dp(aluno):
    lista = []
    dic  = {}
    for alunos in aluno:
         media = (alunos['PI'] + alunos['PF'])/2
         if media < 5:
            lista.append(alunos['matricula'])
    return lista

        

print(notas_dp( [

{'matricula' : 123, 'PI' : 7, 'PF': 3},

{'matricula' : 456, 'PI': 4, 'PF': 8},

{'matricula' : 789, 'PI': 5, 'PF': 1}

]))

