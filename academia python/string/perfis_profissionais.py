def perfis_profissionais(d):
    dr = {}
    dp = {}
    for dinfo in d.values():
        if dinfo['ramo'] not in dp:
            dp[dinfo['ramo']] = 0
        dp[dinfo['ramo']] += 1
        trabalho = dinfo['ramo']
        salario = dinfo['salário'] 
        email = dinfo['e-mail']
        fonte = email[email.find('@')+1:email.find('.com')]
        if trabalho not in dr.keys():
            dr[trabalho] = {}
            dr[trabalho]['média salárial'] = 0
            dr[trabalho]['tempo médio de serviço'] = 0
            dr[trabalho]['servidores'] = []
        dr[trabalho]['média salárial'] += salario
        dr[trabalho]['tempo médio de serviço'] += dinfo['anos de serviço']
        if fonte not in dr[trabalho]['servidores']:
            dr[trabalho]['servidores'].append(fonte)
    for trampo in dr.keys():
        print(trampo)
        result_salario = dr[trampo]['média salárial']/dp[trampo]
        dr[trampo]['média salárial'] = result_salario

        result_tempo = dr[trampo]['tempo médio de serviço']/dp[trampo]
        dr[trampo]['tempo médio de serviço'] = result_tempo
    return dr




print(perfis_profissionais({
    'Pedro Souza': {
        'ramo': 'secretariado',
        'salário': 2500,
        'anos de serviço': 3,
        'e-mail': 'pedro.paulo@hotmail.com'
    },
    'Marisa Monteiro': {
        'ramo': 'odontologia',
        'salário': 6000,
        'anos de serviço': 8,
        'e-mail': 'marisa_monteiro@gmail.com'
    },
    'Vitor Cerqueira': {
        'ramo': 'odontologia',
        'salário': 9000,
        'anos de serviço': 10,
        'e-mail': 'vitorcerqueira@gmail.com'
    },
    'Sandra Gomes': {
        'ramo': 'secretariado',
        'salário': 5000,
        'anos de serviço': 5,
        'e-mail': 'gomes-sandra@uol.com.br'
    },
    'Patrícia Ramos': {
        'ramo': 'vendas',
        'salário': 4000,
        'anos de serviço': 2,
        'e-mail': 'patricia-ramos-1990@yahoo.com.br'
    }
}))

        
        

