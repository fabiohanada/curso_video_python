palavras = ('APRENDER', 'FUTURO', 'PROGRAMAR', 'PYTHON')

for caractere in palavras:
    print(f'\nNa palavra {caractere} temos ', end='')
    for letra in caractere:
        if letra.lower() in 'aeiou':
            print(letra, end='')
