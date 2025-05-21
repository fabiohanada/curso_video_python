n = int(input('Digite um numero para ver a tabuada: '))

for c in range(1, 11):
        resultado = c * n
        print('{} x {} = {}'.format(n, c, resultado))