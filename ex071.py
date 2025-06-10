'''import math

print('-' * 30)
print('BANCO CEV')
print('-' * 30)
valor = float(input('Quer valor voce quer sacar? R$ '))


cedula50 = valor / 50
if cedula50 < 1:
    cedula50 = 0
cedula50t = math.floor(cedula50)
resto50 = valor % 50
cedula20 = resto50/ 20
if cedula20 < 1:
    cedula20 = 0
cedula20t = math.floor(cedula20)
resto20 = resto50 % 20
cedula10 = resto20 / 10
if cedula10 < 1:
    cedula10 = 0
cedula10t = math.floor(cedula10)
resto10 = resto20 % 10
cedula1 = resto10 / 1


print(f'Total de {cedula50t:.0f} cedulas de R$50')
print(f'Total de {cedula20t:.0f} cedulas de R$20')
print(f'Total de {cedula10t:.0f} cedulas de R$10')
print(f'Total de {cedula1:.0f} cedulas de R$1')'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')























