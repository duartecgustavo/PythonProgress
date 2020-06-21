# Desafio 36 - Aula 12 : Programa que aprove o finnciamento para compra de uma casa!
# Programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele pretende pagar
# Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo é negado!

from time import sleep

print('\033[32mBEM VINDO AO PROGRAMA MEU PYTHON, MINHA VIDA!\033[m')

nome = input('Digite seu nome ao lado: ').strip().lower()
idade = int(input(f'E qual a sua idade \033[34m{nome.title()}\033[m? '))

print('\n\033[31maguarde...\033[m')
sleep(1)

print(f'\nCerto \033[34m{nome.title()}\033[m vamos ao finânciamento!')


valor = float(input('\nQual o \033[32mvalor do imóvel\033[m que você deseja comprar? R$ '))
salario = float(input('Agora me diga o valor atual de seu \033[32msalário bruto\033[m: R$ '))
entrada = float(input('E o valor que você possui como entrada?'))
tempo = float(input('Por fim em \033[32mquantos anos\033[m você pretende pagar este valor? '))

valorcomentrada = valor - entrada
salariomax = salario-(salario*(70/100))# O maximo que a pessoa pode assumir como divida é 30% de sua renda
valormeses = valorcomentrada/(tempo*12)# Valor a ser pago por mes

if valormeses <= salariomax: # Caso o valor da prestação seja menor que o valor maximo que a pessoa pode pagar está APROVADO
    print('\n\n\033[34mPARABÉNS! Seu finânciamento foi aprovadissimo!\033[m'
          f'\n\nSeu financiamento será feito em \033[32m{tempo*12:.0f} meses\033[m ou seja \033[32m{tempo:.0f} anos\033[m.'
          f'\nO valor mensal a ser pago será de \033[34mR${valormeses:.2f}\033[m totalizando\032[34mR${valorcomentrada:.2f}\033[m ao fim do finânciamento!')
else:
    print(f'\n\033[31mInfelismente você não pode finânciar este imóvel ainda!\033[m'
          f'\n\nO valor de finânciamento ficou por mês em \033[32mR${valormeses:.2f}\033[m enquanto o valor que você pode finânciar por mês é de \033[31mR${salariomax:.2f}\033[m.')