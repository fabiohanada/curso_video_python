salario = float(input('Qual é o salario do funcionario? '))
aumento = salario + (salario * 15 / 100)

print('Um funcionario que ganhava R${}, com aumento de 15% , passa a receberR${} ' .format(salario, aumento ))