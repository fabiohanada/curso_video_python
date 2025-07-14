'''pessoa = dict()

pessoa['Nome'] = str(input('Nome: '))
pessoa['Media'] = float(input(f'Media de {pessoa['Nome']}: '))

print('-=' * 30)
print(f' - nome é igual {pessoa['Nome']}')
print(f' - media e igual a {pessoa['Media']}')
if pessoa['Media'] > 6:
    print(' - situação é igual a Aprovado')
else:
    print(' - situação é igual a Reprovado')'''

aluno =dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')