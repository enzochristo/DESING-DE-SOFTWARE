def eh_crescente(l):
    i = 0
    while i < len(l) - 1  :
        anterior = l[i]
        i += 1
        proximo = l[i]

        if proximo <= anterior:
         return False
    return True

print(eh_crescente([1,1,1,1]))