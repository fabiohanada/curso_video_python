from datetime import  date
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print('O atleta tem {} anos'.format(idade))

if idade < 9:
    print('Classificacao: MIRIN')
elif idade > 9 and idade <= 14:
    print('Classificacao: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificacao: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificacao: SENIOR')
else:
    idade > 25
    print('MASTER')