"""viagem = float(input('Qual e a distancia da sua viagem?'))
print('Voce esta prestes a comecar a sua viagem de {} km'.format(viagem))
viagem1 = (viagem * 0.5)
viagem2 = (viagem * 0.45)
if viagem <= 200:
    print('E o preco da sua passagem sera de R${}'.format(viagem1))
else:
    print('E o preco da sua passagem sera de R${}'.format(viagem2))"""

distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('E o preco da sua pasagem sera de R${:.2f}'.format(preco))