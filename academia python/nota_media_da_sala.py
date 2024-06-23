def nota_quizzes(q1 , q2 , q3 , q4 , q5):
 if q1 < 0 or q2 > 10 or q2 < 0 or q2 > 10 or q3 < 0 or q3 > 10 or q4 < 0 or q4 > 10 or q5 < 0 or q5 > 10:
  return 0
 soma = q1 + q2 + q3 + q4 + q5
 menor = q1
 if q2 < menor :
  menor = q2
 if q3 < menor :
   menor = q3
 if q4 < menor :
    menor = q4
 if q5 < menor :
     menor = q5

 return (soma - menor) / 4


def nota_final (media_quiz , av_interm , av_final , ep1 , ep2  , pf):
    if media_quiz <0 or media_quiz > 10 or av_interm <0 or av_interm > 10 or av_final <0 or av_final > 10 or  ep1<0 or ep1 > 10 or ep1 <0 or ep2 > 10 or ep2 <0 or pf > 10 or pf < 0 :
        return 0
    ni = 0.4 * av_interm + 0.5 * av_final + .1 * media_quiz
    ng = .1 * ep1 + .2*ep2 + .7*pf
    result = ni
    if ni < 5 or ng < 5 :
         if  result > ng :
            result = ng
    else :
        result = (ni+ng)/2
    return result

aprovado = 0
reprovado = 0
soma = 0
i = 0
continuar = True
interesse = 0
media = 0
tx_aprovados = 0
tx_reprovados = 0
p1 = input('Quer adicionar nota ?')


while continuar :
 i +=1
 if p1 == 'nao' or p1 == 'não' :
   continuar = False
 else:
  q1=float (input ('q1: '))
 
  q2=float (input ('q2: '))

  q3=float (input ("q3: "))

  q4=float (input ('q4: '))

  q5=float (input ('q5: '))

  ai=float (input('ai: '))

  af=float (input('af: '))

  ep1=float (input('ep1: '))

  ep2=float (input('ep2: '))

  pf=float (input('pf: '))
  
  media_quizes = nota_quizzes(q1,q2,q3,q4,q5)

  interesse = nota_final(media_quizes,ai,af,ep1,ep2,pf)

  if interesse >= 5 : 
   aprovado += 1
  else :
   reprovado +=1

  print(f'Nota final do aluno:{interesse:.2f}')

  soma += interesse
  media = soma/i 
  tx_aprovados = (aprovado/i) * 100
  tx_reprovados = (reprovado/i) * 100
  p1 = input('Quer adicionar nota ?')
 

 
 print(f'Média da sala: {media:.2f}')
 print(f'Aprovados: {tx_aprovados:.2f}%')
 print(f'Reprovados: {tx_reprovados:.2f}%')








