from datetime import date
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
alistamento = (ano + 18)
idade = ano_atual - ano
print('Quem nasceu em {} tera {} anos em {}'. format(ano, ano_atual - ano, ano_atual))
if  idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(alistamento - ano_atual))
    print('Seu alistamento sera em {}'.format(alistamento))
elif idade > 18:
    print('Voce ja deveria ter se alistado ha {} anos.'.format(ano_atual - alistamento))
    print('Seu alistamento foi em {}.'.format(alistamento))
else:
    idade = 18
    print('Aliste se imediatamente')
