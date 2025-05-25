'''from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
c = 0
while c == 0:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>>>> Qual é a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
        print('==--==--==--==--==--==--==')
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicacao entre {} x {} é {}'.format(n1, n2, multi))
        print('==--==--==--==--==--==--==')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            n2 > n1
            maior = n2
        print('O maior numero é {}'.format(maior))
        print('==--==--==--==--==--==--==')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        if opcao == 5:
            print('Finalizando...')
            print('==--==--==--==--==--==--==')
            print('Fim do programa! Volte Sempre!')
            break
        else:
            print('Opcao invalida. Tente novamente')
            print('==--==--==--==--==--==--==')
    sleep(2)'''


from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre')


