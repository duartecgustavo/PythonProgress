# Desafio 36 - Aula 12 : Programa que aprove o finnciamento para compra de uma casa!
# Programa deve perguntar o VALOR da casa, o SALARIO do comprador e em quantos ANOS ele pretende pagar.
# Calcular o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o emprestimo é negado!

from time import sleep

print('*'*50)
print(f'\033[32m{"BEM VINDO AO PROGRAMA MEU PYTHON, MINHA VIDA!":^50}\033[m')
print('*'*50)

nome = input('Digite seu nome ao lado: ').strip().lower()
idade = int(input(f'E qual a sua idade \033[34m{nome.title()}\033[m? '))

print('\n\033[31maguarde...\033[m')
sleep(1)

print(f'\nCerto \033[34m{nome.title()}\033[m, vamos ao finânciamento!')
print(f'-'*50)


valor = float(input('\n\033[32mValor do imóvel\033[m que você deseja comprar? R$'))
print(f'_'*25)
salario = float(input('Valor atual de seu \033[32msalário bruto\033[m: R$ '))
print(f'_'*25)
entrada = float(input('Valor que você possui como entrada?'))
print(f'_'*25)
tempo = float(input('\033[32mPor quantos anos\033[m você pretende pagar este valor? '))
print(f'_'*25)

valorcomentrada = valor - entrada
salariomax = salario-(salario*(70/100))
# O maximo que a pessoa pode assumir como divida é 30% de sua renda
valormeses = valorcomentrada/(tempo*12)
# Valor a ser pago por mes

if valormeses <= salariomax:
# Caso o valor da prestação seja menor que o valor maximo que a pessoa pode pagar está APROVADO
    print('\n\n\033[34mPARABÉNS! Seu finânciamento foi aprovadissimo!\033[m'
          f'\n\nSeu financiamento será feito em \033[32m{tempo*12:.0f} meses\033[m ou seja \033[32m{tempo:.0f} anos\033[m.'
          f'\nO valor mensal a ser pago será de \033[34mR${valormeses:.2f}\033[m totalizando\032[34mR${valorcomentrada:.2f}\033[m ao fim do finânciamento!')
else:
    print(f'\n\033[31mNEGADO!\033[m Infelismente você não pode finânciar este imóvel ainda!'
          f'\n\nO valor de finânciamento ficou por mês em \033[32mR${valormeses:.2f}\033[m enquanto o valor que você pode finânciar por mês é de \033[31mR${salariomax:.2f}\033[m.')