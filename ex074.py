'''from random import randint

n1 = randint(1, 9)
n2 = randint(1, 9)
n3 = randint(1, 9)
n4 = randint(1, 9)
n5 = randint(1, 9)

tupla = (n1, n2, n3, n4, n5)

print(f'Os valores sorteados foram: {tupla}')'''

from random import randint
numeros = (randint(1, 10), randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))

#print(f'Eu sorteei os valores {n}')

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')



