'''num = []
valor = 5
while True:
    num.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer contuinuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        num.sort(reverse=True)
        tamanho = len(num)
        print(f'Voce digitou {tamanho} elementos')
        print(f'Os valores em ordem descrescete sao {num}')
        if valor in num:
            print(f'O valor {valor} faz parte da lista!')
        else:
            print(f'O valor {valor} não foi encontrado na lista!')
        break'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi enocntrado na lista!')