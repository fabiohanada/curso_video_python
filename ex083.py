'''expressao = input('Digite a expressão: ')
quantidade_parenteses_abertura = expressao.count('(')
quantidade_parenteses_fechamento = expressao.count(')')

if quantidade_parenteses_abertura == quantidade_parenteses_fechamento:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta errada!')'''

expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão esta errada')