print('Gerador de PA')
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
while primeiro <= 70:
    primeiro = primeiro + razao
    print(primeiro)

