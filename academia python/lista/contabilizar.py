def contabilizar(volume,lista):
    quantidade = 0
    resto = 0
    for garrafa in lista:
            vezes = garrafa[1]
            litro = garrafa[0]*vezes
            quantidade += litro//volume
            resto += (litro/volume) - litro//volume
            if resto >= 1:
                  resto -= int(resto)
                  quantidade += 1
    return quantidade

print(contabilizar(1700, [[3850,8],[600,80],[3600,96],[1450,14],[900,100],[4100,22],[650,95],[2150,100],[550,73],[1600,70],[3000,7],[1250,53],[400,23],[3100,70],[3650,43],[3800,40]]))

            

