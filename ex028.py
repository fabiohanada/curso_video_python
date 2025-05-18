"""print('Vou pensar em um numero entre 0 e 5. Tente advinhar')
n = int(input('Em que numero eu pensei: '))
print('PROCESSANDO')
if n == 0:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero 0 e nao no 3!')"""

from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?'))
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}'.format(computador, jogador))