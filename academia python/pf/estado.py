def limpa_string(string):
    string = string.lower()
    interesse = string[19:].split()
    l = []
    for palavras in interesse:
        if palavras == 'online' or palavras== 'parado':
            l.append(palavras)
    return interesse

def estado(logs):
    d = {}
    for info in logs:
        palavra = limpa_string(info)
        info = info[11:19].split()
    if 


print(estado(['2023-08-14 08:50:12 Falha código 467 - Sistema Online',
'2023-08-14 13:50:12 Online',
'2023-08-14 23:50:11 Sistema Parado após erro inexperado',
'2023-08-14 23:12:45 Sistema reiniciado, está Online']
))