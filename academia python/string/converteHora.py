def converteHora(h):
    if int(h[:2]) >= 12:
        if h[:2] == '12':
            return h[:2] + h[2:] + ' PM'
        result = int(h[:2])  - 12 
        hora = '0' + str(result) + h[2:] + ' PM'
    else:
       hora  = h + ' AM'
       if h[:2] == '00':
           return '12' + h[2:] + ' AM'
    return hora
print(converteHora('12:00'))




        

