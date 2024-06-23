def inicia_jogo(n,lp):
    lista = []
    dj = {}
    dm = {}
    dmesa = {}
    dt = {'jogadores': {}}
    for x in range(len(lp)//7):
        lista.append(lp[x*7:7*(1+x)])
    for i in range(len(lista)):
        if i >= n:
            r = len(lista) - n 
            dt['monte'] = lista[r:len(lista)]
            break

        else: 
            dj['jogadores'][i] = lista[i]
            dt = dj
    dt['mesa'] = []
    return dt




def inicia_jogo(n,lp):
    jog = {}
    dt = {}
    for i in range(n):
        jog[i] = lp[i*7:7*(i+1)]
    
    monte = lp[7*n:]
    dt['jogadores'] = jog
    dt['monte'] = monte
    dt['mesa'] = {}
    return dt



print(inicia_jogo(2,[
	[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
	[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
	[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
	[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]
))

