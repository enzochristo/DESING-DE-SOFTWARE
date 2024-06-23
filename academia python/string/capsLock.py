def capsLock(s):
    p = ''
    for l in s:
        if l != l.lower():
            l = l.lower()
            p += l 
        else:
            l = l.upper()
            p+=l
    return p

            
