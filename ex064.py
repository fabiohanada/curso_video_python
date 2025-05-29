cont = 0
soma = 0
while cont != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:

        cont += 1
        soma += n
    else:
        print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
        break

