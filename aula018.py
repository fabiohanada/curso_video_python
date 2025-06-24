num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')


if 4 in num:
    num.remove(4)
else:
    print('Nao contem')

for cont in range(0,5):
    num.append((int(input('Digite um valor: '))))

for c, v in enumerate(num):
    print(f'{c} {v}')

