totmulher20 = 0
tothomem = 0
mais18 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    print('-' * 30)
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        tothomem += 1
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if continua in 'Nn':
        print(f'Total de pessoas com mais de 18 anos: {mais18}')
        print(f'Ao todo temos {tothomem} homens cadastrados')
        print(f'E temos {totmulher20} mulheres com menos de 20 anos.')
        break