print('===================')
print('10 TERMOS DE UMA PA')
print('===================')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, '->', end=' ')
print('Acabou')
