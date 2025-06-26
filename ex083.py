expressao = input('Digite a expressão: ')
quantidade_parenteses_abertura = expressao.count('(')
quantidade_parenteses_fechamento = expressao.count(')')

if quantidade_parenteses_abertura == quantidade_parenteses_fechamento:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta errada!')