def atualiza_telefone(cel):
    if cel.find('-') == -1:
        if len(cel) == 8:
            cel = '9'+ cel[:4] + '-' + cel[4:] # tem que ir continuar exatamente de onde se parou.
        else:
            cel = cel[:5] + '-' + cel[5:]
    else: 
         if len(cel) == 9:
            cel = '9'+ cel
    return cel

print(atualiza_telefone('72727226'))
             