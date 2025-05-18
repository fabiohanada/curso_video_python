velocidade = int(input('Qual e a velocidade atual do carro?'))

if velocidade > 80:
    print('MULTADO! Voce excedeu o limite que e de 80km')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com seguranca!')

