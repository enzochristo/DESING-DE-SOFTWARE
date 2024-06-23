def eh_fibonacci(lista):
    if len(lista) < 3 :
        return False
    for el in range(2,len(lista),1):
        if lista[el] == lista[el-1] + lista[el-2] :
            resp = True
        else:return False
    return resp
        

print(eh_fibonacci([1,2,3,4,5,6,7,8,9,10]))


