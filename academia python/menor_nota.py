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
        
