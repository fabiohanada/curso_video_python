'''a = 0
b = 1
contador = 0
numero_termos = int(input('Digite o numero de termos: '))
while contador < numero_termos:
    print(' -> {}'.format(a), end='')
    prox_termo = a + b
    a = b
    b = prox_termo
    contador += 1'''

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')



