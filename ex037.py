n = int(input('Digite um numero:'))
print('Escolha uma base para converter')
print('[1] binario')
print('[2] octal')
print('[3] hexa')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    binario = bin(n)
    print(binario[2:])
elif opcao == 2:
    octal = oct(n)
    print(octal[2:])
else:
    opcao == 3
    hexa = hex(n)
    print(hexa[2:])