n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a media do aluno e {}'.format(n1, n2, media))
if media >= 7:
    print('aprovado')
elif media >= 5.1 and media <= 6.9:
    print('recuperacao')
else:
    media < 5
    print('Reprovado')