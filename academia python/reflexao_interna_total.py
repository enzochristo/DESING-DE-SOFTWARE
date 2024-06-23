import math
def reflexao_total_interna(n1,n2, teta_2):
    teta_2_rad = math.radians(teta_2)
    sin_teta_1_rad = n2/n1 * math.sin(teta_2_rad)
    return sin_teta_1_rad > 1
      # quando tem esse > 1 ele vai retornar um verdadeiro ou falso , por ser uma variavel booleana , entao automaticamente ja sera esse modo de resposta 
