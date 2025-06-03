n = 0
while n > -1:
    n = 0
    cont = 0
    m = 0
    n = int(input('Quer ver a tabuada de qual valor? '))
    while cont < 10:
        cont += 1
        m = n * cont
        print(f'{n} x {cont} = {m}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')