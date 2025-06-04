while True:
    n = 0
    cont = 0
    m = 0
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n > 0:
        while cont < 10:
            cont += 1
            m = n * cont
            print(f'{n} x {cont} = {m}')
    else:
        n < 0
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
        break

'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''

