'''from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue advinhar qual foi?')
n = int(input('Qual e seu palpite? '))
computador = randint(0, 10)
c = 1

while c < 11:
    if n == computador:
        print('acertou')
        break
    else:
        c = c + 1
        if n < computador:
            print('mais, tente novamente')
            n = int(input('Qual e seu palpite? '))
            print('Voce acertou em {} vezes.'.format(c))
        else:
            print('menos, tente novamente')
            n = int(input('Qual e seu palpite? '))
            if n == computador:
                print('Voce acertou em {} vezes.'.format(c))
                break'''

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            jogador > computador
            print('Menos, Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens'.format(palpites))
