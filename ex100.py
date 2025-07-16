'''from random import randint

def numeros(a, b, c, d, e):
    print(f'Sorteando 5 valores da lista: {a, b, c, d, e} PRONTO!!')
    if a % 2 == 0:
        par1 = a
    else:
        par1 = 0
    if b % 2 == 0:
        par2 = b
    else:
        par2 = 0
    if c % 2 == 0:
        par3 = c
    else:
        par3 = 0
    if d % 2 == 0:
        par4 = d
    else:
        par4 = 0
    if e % 2 == 0:
        par5 = e
    else:
        par5 = 0
    partot = par1 + par2 + par3 + par4 + par5
    print(f'Somando os valores pares de {a, b, c, d, e}, temos {partot}')

numeros(randint(0, 10), randint(0,10), randint(0, 10), randint(0,10), randint(0, 10))'''
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)






















