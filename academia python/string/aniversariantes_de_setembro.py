def aniversariantes_de_setembro(d):
    dic = {}
    for nome, data in d.items():
        if int(data[4:5]) == 9:
            if nome not in dic:
                dic[nome] = ''
            dic[nome] += data
    return dic

print(aniversariantes_de_setembro({'Nico Uno': '01/01/1992', 'Horácio P. Genaro': '03/03/1992', 'Ukibe Nokome': '05/05/1992', 'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}))