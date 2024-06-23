salario_bruto = float(input('qual o salario bruto ? '))
numero = int(input('qual o numero de dependentes ? '))
aliquota = 0
c = 189.59
deducao = 0
if salario_bruto <= 1045 :
    aliquota = 0.075*salario_bruto
elif salario_bruto >= 1045.01 and salario_bruto <= 2089.60:
    aliquota = 0.09*salario_bruto
elif salario_bruto >=2089.61 and salario_bruto <= 3134.40:
    aliquota = 0.12*salario_bruto
elif salario_bruto >=3134.41 and salario_bruto <= 6101.06 :
    aliquota = 0.14*salario_bruto
else: aliquota = 671,12


base_de_calc = salario_bruto - aliquota - (numero * c)

if base_de_calc <= 1903.98 : 
    aliquota = 0
    deducao = 0
elif base_de_calc >= 1903.99 and base_de_calc <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base_de_calc >= 2826.66 and base_de_calc <= 3751.05 : 
    aliquota = 0.15
    deducao = 354.80
elif base_de_calc >= 3751.06 and base_de_calc <= 4664.68 :
    aliquota = 0.225
    deducao = 636.13
else :
    aliquota = 0.275
    deducao = 869.36

irrf = (base_de_calc * aliquota )- deducao



print(irrf)