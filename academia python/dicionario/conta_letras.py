def conta_letras(palavra):
    dic = {} 
    for letra in palavra:
        if letra not in dic:
            dic[letra] = 0
        dic[letra] +=1
print(conta_letras('banana da terra'))

 

        