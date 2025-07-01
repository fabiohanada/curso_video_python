'''pessoa = list()
dado = list()
pessoas = 0
maior = 0
menor = 999
while True:
    dado.append(str(input('Nome: ')))
    dado.append((float(input('Peso: '))))
    pessoa.append(dado[:])
    dado.clear()
    pessoas += 1

    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break

for p in pessoa:
    if p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]

print(f'Ao todo, voce cadastrou {pessoas} pessoas. ')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for a in pessoa:
    if a[1] == maior:
        print(f'[{a[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for b in pessoa:
    if b[1] == menor:
        print(f'[{b[0]}] ', end='')'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(princ)
print(f'Ao, todo, voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()


