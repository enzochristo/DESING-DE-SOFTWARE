def quando_passa(d, title):
    d2 = {}
    for canal,horarios in d.items():
        for hora,filmes in horarios.items():
            if title in filmes:
                if hora not in d2:
                    d2[hora] = []
                d2[hora].append(canal)
                #ou pode ser feito assim:
                    #lista = d2[hora]
                    #lista.append(canal)
                    #d2[hora] = lista
    return d2
            
                
    
print(quando_passa({
    'Raposa TV': {
        '00h00': 'ModSim: Tudo é Possível',
        '01h00': 'Férias em Mathland',
        '07h00': 'Hora do Relaxamento',
        '15h00': 'Vale a Pena Rever a Matéria',
        '23h30': 'DesSoft: Hacking the Server'
    },
    'INN': {
        '08h00': 'Notícias do Campus',
        '10h00': 'Futuro: Intercâmbio',
        '12h00': 'Tele curso: Cálculo IV',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Vale a Pena Rever a Matéria',
        '22h00': 'Culinária dos Salgados'
    },
    'Rede Insper TV': {
        '07h00': 'Hora do Relaxamento',
        '13h00': 'Campus em Foco',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Hora do Relaxamento',
        '21h00': 'Futuro: Intercâmbio'
    }
}, 'Hora do Relaxamento'))
        