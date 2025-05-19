casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = float(input('Quantos anos de financiamento? '))
prestacao = casa /(anos * 12)
porcentagem = salario * 0.30
print('Para pagar uma casa de R${} em {} anos a prestação sera de {}'.format(casa, anos, prestacao))
if prestacao <= porcentagem:
    print('Concedido')
else:
    print('Negado')

