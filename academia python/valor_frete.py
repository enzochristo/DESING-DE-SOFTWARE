def calcula_frete (vt , qtd , fragil , distancia ):
    vb = 12.75
    vkm = 1.82
    cx = qtd // 40
    if fragil == 'S':
        vs = vt * 0.0175
    else : 
        vs = vt * 0.008
    if qtd % 40 != 0 :
        cx += 1 

    
    vf = vb + (cx * vkm * distancia) + vs
    return vf
    
print (calcula_frete(800.99, 135 , 'S' , 65.6))


