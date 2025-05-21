peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m)'))
imc = peso/(altura * altura)
print('O IMC da pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO')
elif imc > 18.6 and imc < 25:
    print('Voce esta no PESO IDEAL')
elif imc > 25.1 and imc < 30:
    print('Voce esta com SOBREPESO')
elif imc > 30.1 and imc < 40:
    print('Voce esta com OBESIDADE')
else:
    print('Cuidado voce esta com OBESIDADE MORBIDA')
