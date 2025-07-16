'''def conta():
    total = larg * comp
    return total

print('Controle de Terrenos')
print('-' * 40)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

print(f'A area de um terreno {larg} x {comp} é de {conta()}m2')'''

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m2.')

print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m):'))
area(l, c)