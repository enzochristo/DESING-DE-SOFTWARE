p1 = input("Deseja inserir um novo aluno? [S/N]") =='S'
menor_nota_ai = 0

menor_nota_af = 0

menor_nota_geral = 0

maior_media = 0

media_ai = 0

media_af = 0

soma_af = 0

soma_ai = 0

contador = 0



while p1 :
    ai = float(input("Qual a nota na AI? "))

    af = float(input("Qual a nota na AF? "))

    if contador == 0 :
        menor_nota_ai = ai
        menor_nota_af = af

    soma_af += af
    soma_ai += ai
    media = ai*.4 + af*.6

    if menor_nota_ai > ai :
        menor_nota_ai = ai

    if menor_nota_af > af :
        menor_nota_af = af

    if menor_nota_af > menor_nota_ai:
        menor_nota_geral = menor_nota_ai
    else: menor_nota_geral = menor_nota_af

    if media > maior_media :
        maior_media = media

    p1 = input("Deseja inserir um novo aluno? [S/N]") == 'S'
    contador += 1

media_af = soma_af/contador
media_ai = soma_ai/contador
    
    
print(f"A menor nota em avaliações foi {menor_nota_geral:.1f}")

print(f"A maior média final foi {maior_media:.1f}")

print(f"A média das notas da AI foi {media_ai:.1f}"
)

print(f"A média das notas da AF foi {media_af:.1f}")