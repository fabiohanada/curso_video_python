def voto():
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 18:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif 18 < idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATORIO')
    else:
        return print(f'Com {idade} anos: VOTO OPCIONAL')

print('-' * 30)
nasc = int(input('Em que ano voce nasceu? '))
voto()

'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade or idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'

nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))'''