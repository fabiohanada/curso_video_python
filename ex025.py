"""nome = str(input('Qual é o seu nome completo? '))
te = 'Silva' in nome
print('Seu nome tem Silva? ' + str(te))"""

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome em Silva? {}'.format('silva' in nome.lower()))