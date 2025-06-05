'''from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
g = 0
cont = 0
while True:
    num = int(input('Diga um valor: '))
    situacao = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    computador = randint(1, 10)
    soma = num + computador
    res = soma
    print('=-' * 30)
    if res % 2 == 0 and situacao in 'Pp':
        print(f'Voce jogou {num} e o computador {computador}. Total de {soma} deu PAR' )
        print('Voce venceu')
        print('Vamos jogar novamente...')
        cont += 1
    elif res % 2 == 0 and situacao in 'Ii':
        g = 1
        print(f'Voce jogou {num} e o computador {computador}. Total de {soma} deu PAR' )
        print('Voce perdeu')
        print(f'GAME OVER! Voce venceu {cont} vezes.')
    elif res % 2 == 1 and situacao in 'Pp':
        g = 1
        print(f'Voce jogou {num} e o computador {computador}. Total de {soma} deu IMPAR' )
        print('Voce perdeu')
        print(f'GAME OVER! Voce venceu {cont} vezes.')
    elif res % 2 == 1 and situacao in 'Ii':
        print(f'Voce jogou {num} e o computador {computador}. Total de {soma} deu IMPAR' )
        print('Voce ganhou')
        print('Vamos jogar novamente...')
        cont += 1
    if g == 1:
        break'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')








