'''num = [9, 4, 9 , 1, 1]

# for cont in range(0, 5):
#     num.append(int(input(f'Digite um valor para a posição {cont}: ')))

for pos, item in enumerate(num):
    print(f'Na posicao {pos} temos o item {item}')

print(f'O maior valor digitado foi {max(num)} nas posicoes {num.index(max(num))}... {pos}...')'''

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c ==0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if  listanum[c] < men:
            men = listanum[c]
print(('=-' * 30))
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()

