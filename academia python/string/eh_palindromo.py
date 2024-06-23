def eh_palindromo(s):
    resp = True
    a = s[:]
    b = s[-1::-1]
    if a == b:
        return resp
    return False

print(eh_palindromo('roma é amor'))