nome = str(input('Digite o sue nome: '))
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minisculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)))
primeiro = nome.split(" ")[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro, len(primeiro)))

