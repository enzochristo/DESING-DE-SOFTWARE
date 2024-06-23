def conserta_teclado(s):
    if s == '':
        return ''
    p = s[0].lower()
    for i in range(1,len(s)):
        if s[i].lower() != s[i-1].lower() :
            p+= s[i].lower()
      
    return p





print(conserta_teclado(''))