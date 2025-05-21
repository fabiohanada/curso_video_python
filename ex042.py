r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3> r2 and r2 + r3 > r1:
    print('Os segmentos PODEM FORMAR um triangulo', end=' ')
    if r1 == r2 and r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Os segmentos NAO PODEM FORMAR um triangulo!')