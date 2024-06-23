def eh_valida(eq):
    d_eq = {'(':')','[':']','{':'}'}
    r = ''
    i = 0
    for s in eq:
        if s in d_eq:
            r+= s
        elif s in d_eq.values():
            r+= s

    if len(r)%2 != 0:
        return False
    
    if len(r) == 2:
        if r[0] != '(':
            return False
    if len(r) == 4:
        if r[0] !='(' and r[1] !='[':
            return False
    if len(r) >= 6:
        if r[0] !='(' and r[1] !='[' and r[2] != '{':
            return False

    while i < len(r)/2:
        a = r[i]
        b = r[-i-1]
        if d_eq[r[i]] == r[-i-1]:
            pass
        else: return False
        i += 1
    return True


print(eh_valida("({[1 + 2]}* 7 + (4/2))"))
        


        



        

