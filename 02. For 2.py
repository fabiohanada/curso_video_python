""" 
Calcular o Salário Anual

Pede-se:

Solicitar ao usuário o salário mensal inicial
e o percentual de aumento mensal.
Usar o laço for para calcular o salário 
acumulado mês a mês ao longo de 12 meses.
Exibir o salário de cada mês e o total ao final.


Entrada
=======

    Digite o salário mensal inicial: 2000
    Digite o aumento percentual mensal: 2

    SAÍDA
    =====
    Mês 1: 000.00
    Mês 2: 000.00
    Mês 3: 000.00
    Mês 4: 000.00
    ...
    Mês 12: 000.00
    Salário total no ano: R$ 000.00
    
 """
# Escreva seu código aqui

#1passo
salario_mensal = input('Digite o salario: ')

valor_formato = salario_mensal.replace('.','').replace(',','.')

#converter para float
sal_mensal = float(valor_formato)

#2 passo
percentual_aumento = float(input('Digite o percentual: '))

# 3passo inicializar o total acumulado
salario_total = 0

# 4 passo exibir o print
print('Salarios ao longo dos 12 meses')

# 5 passo calcular 

mes = 1
for mes in range(13):
    print(f'Mes {mes} : R$ {sal_mensal:.2f}')

    salario_total = salario_total + sal_mensal
    sal_mensal = sal_mensal + (sal_mensal * percentual_aumento)




















































































































