def meta_atingida ( lim_reclamacoes , lim_justica , prop_rec , prop_justica ):
    return lim_reclamacoes >= prop_rec and lim_justica >= prop_justica 

  
    

a = float(input('limite 1 '))

b =float(input('limite 2 '))

c =float(input('prop 1 '))

d = float(input('prop 2 '))

print(meta_atingida(a,b,c,d))