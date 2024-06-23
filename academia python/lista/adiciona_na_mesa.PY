def adiciona_na_mesa(peca,mesa):
    if mesa == []:
        mesa.append(peca)
        return mesa
    
    mesa_antiga = mesa
    for el in range(len(peca)):
        if peca[el] == mesa[0][0]:
            del(mesa)
            mesa = []
            peca = [peca[el-1],peca[el]]
            mesa.append(peca)
            for lista in range(len(mesa_antiga)):
                mesa.append(mesa_antiga[lista])
            return mesa
        elif peca[el] == mesa[-1][1]:
            if el == 1 : 
                peca = [peca[el],peca[el-1]]    
            mesa.append(peca)
            return mesa
        
   

print(adiciona_na_mesa([1,6],[[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6]]))

