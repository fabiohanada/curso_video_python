'''valores = []

for c in range(4):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

tupla_nova = tuple(valores)

print(f'O valor 9 apareceu {tupla_nova.count(9)} vezes')
print(f'O valor 3 apareceu na posiçao {tupla_nova.index(3)+1}')'''

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparceu na {num.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

