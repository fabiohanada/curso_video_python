"""nome = str(input('Qual seu nome? '))
if nome == 'Fabio':
    print('Que nome lindo')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
print('A sua media foi {}'.format(m))
if m >=6:
    print('parabens')
else:
    print('estude mais')