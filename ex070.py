'''total = 0
cont = 0
barato = 999999
novo_prod = ' '
print('-' * 30)
print('LOJA SUPER BARATAO')
print('-' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    continua = str(input('Quer continuar? [S/N] '))
    total += preco
    if preco > 1000:
        cont += 1
    if preco < barato:
        barato = preco
        novo_prod = produto
    if continua in 'Nn':
        print(f'O total da compra foi R${total}')
        print(f'Temos {cont} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {novo_prod} que custa R${barato}')
        break'''

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total =+ preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
































