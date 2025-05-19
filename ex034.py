salario = float(input('Qual e o salario do funcionario? R$ '))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print('Quem ganhava R${} passa a ganhar R${} agora'.format(salario, aumento))