a = input('digite uma quantidade de dias ')
b = input('digite uma quantidade de horas ')
g = input('digite uma quantidade de minutos ')
c =input('digite uma quantidade de segundos ')


i= int(a)
e= int(b)
f= int(g)
g= int(c)

def total_em_segundos(d , h , m , s):
 conta_de_dias_em_seg = i * 86400
 conta_de_horas_em_seg = e * 3600
 conta_de_minutos_em_seg = f * 60
 conta_de_segundos = g +  conta_de_dias_em_seg + conta_de_horas_em_seg + conta_de_minutos_em_seg
 return conta_de_segundos

print((total_em_segundos(i,e,f,g)))

#pq ta diferente do oi.py ? #
