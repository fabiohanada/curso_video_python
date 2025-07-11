from random import randint
from time import sleep

print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)
cont = 0
vezes = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {vezes} JOGOS -=-=-=')

while True:
    n1 = randint(1, 60)
    n2 = randint(1, 60)
    n3 = randint(1, 60)
    n4 = randint(1, 60)
    n5 = randint(1, 60)
    n6 = randint(1, 60)
    num_sort = [n1, n2, n3, n4, n5, n6]
    num_sort.sort()
    print(num_sort)
    sleep(1)
    cont += 1
    if cont == vezes:
        break
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
#arrumar a repeticao

'''from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)'''























