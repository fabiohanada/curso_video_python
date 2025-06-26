'''lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print(f'A lista completa é {lista}')
        print(f'A lista de pares é {par}')
        print(f'A lista de impares é {impar}')
        break'''

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str (input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

