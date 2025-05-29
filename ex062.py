'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
decimo = primeiro + (10 - 1) * razao
while primeiro <= decimo:
    print('{}'.format(primeiro), end='')
    print(' -> ' , end='')
    primeiro = primeiro + razao
print('PAUSA')
termo = int(input('Quantos termos voce quer mostrar a mais? '))
quantidade = primeiro + termo
while primeiro <= quantidade:
    primeiro = primeiro + razao
    print(primeiro)'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))
print('FIM')
