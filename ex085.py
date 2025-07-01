numero = list()
par = list()
impar = list()

for c in range(0, 7):
    numero.append(int(input(f'Digite o {c+1}o valor: ')))
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

numero.clear()
numero.append(par)
numero.append(impar)
print('-=' * 30)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores impares digitados foram: {numero[1]}')

'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' *  30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')'''
