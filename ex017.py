c_oposto = float(input('Comprimento do cateto oposto: '))
c_adjacente = float(input('Comprimento do cateto adjacente: '))

q1 = c_oposto ** 2
q2 = c_adjacente ** 2

soma = q1 + q2

hip = soma ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hip))