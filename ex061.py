'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
decimo = primeiro + (10 - 1) * razao
while primeiro <= decimo:
    print('{}'.format(primeiro), end='')
    print(' -> ' , end='')
    primeiro = primeiro + razao
print('FIM')'''


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

