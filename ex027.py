nome = str(input('Digite seu nome completo: ')).strip()

dividido = nome.split()
print('Prazer em te conhecer')
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu ultimo nome é {}'.format(dividido[len(dividido)-1]))