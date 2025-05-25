sexo = 'M'

while sexo == 'M':
    sexo1 = str(input('Informe seu sexo: [M/F] ')).strip()
    if sexo == sexo1:
        print('Sexo {} registrado.'.format(sexo1))
        break
    elif sexo1 == 'F':
        print('Sexo {} registrado.'.format(sexo1))
        break
    else:
        sexo != sexo1
        print('Dados invalidos.')

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))'''