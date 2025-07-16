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

# 1o passo - solicitar o salário inicial
salario_mensal = input('Digite o salário no formato 000.000,00')

# precisamos transformar o valor de entra no padrão 
# Americano = 000,000.00
# Exemplo: 1,890.00
valor_formato = salario_mensal.replace('.','').replace(',','.')

# converter para float
sal_mensal = float(valor_formato)

# 2o passo - converter o percentual para decimal
percentual_aumento = float(input('Digite o percentual:'))

# leia-se: percentual_aumento = percentual_aumento / 100
percentual_aumento /= 100

# 3o passo - inicializar o total acumulado
salario_total = 0

# 4o passo - exibir print
print('\nSalários ao longo dos 12 meses:')

# 5o passo - Calcular os salários mês a mês
# range(13) = doze meses (limite do processamento)
#mes = 1
for mes in range(1, 13):

    print(f'Mês {mes} : R$ {sal_mensal:,.2f}'
          .replace(',','texto').replace('.',',').replace('texto','.'))
    
    salario_total = salario_total + sal_mensal
    sal_mensal = sal_mensal + (sal_mensal * percentual_aumento)

# sai do for *** cuidado para não perde-se ***

# 6o passo - formatar o total no estilo brasileiro
salario_total_formatado = f'{salario_total:,.2f}'.replace(',','texto'.replace('.',',')
                         .replace('texto','.'))

# 7o passo - exibir o salário total
print(f'\nSalário total ao longo do ano: R$ {salario_total_formatado}')
































































































