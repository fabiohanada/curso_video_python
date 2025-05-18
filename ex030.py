"""n = int(input('Me diga um numero:'))

if n % 2 == 0:
    print('par')
else:
    print('impar')"""

numero = int(input('Me diga um numero:'))
resultado = numero % 2
if resultado == 0:
    print('O numero {} e PAR'.format(numero))
else:
    print('O numero {} e IMPAR'.format(numero))