# Desafio 34 - Aula 10: Programa que leia o salario de um funiconario e calcule o aumento
# Salarios acima de  de R$1250 o aumento é de 10%
# Sarios inferiores ou iguais o aumento é de 15%

nome = input('Olá, qual é o seu nome? ')

salario = float(input(f'\033[34m{nome.title()}\033[m, digite seu \033[32msalario atual\033[m para reajustarmos \033[4mseu aumento\033[m: '))

if salario <= 1250:
    salarioaumento = salario+(salario*(15/100))
if salario > 1250:
    salarioaumento = salario+(salario*(10/100))

print(f'O \033[32maumento\033[m foi de \033[34mR${salarioaumento-salario}\033[m')
print(f'Agora você recebera mensalmente \033[34mR${salarioaumento}\033[m')

'''if salario <= 1250:
    print(f'{nome.title()}, seu salário terá um aumento de 15%, agora passará a receber R${salario+(salario*(15/100)):.2f}')
if salario > 1250:
    print(f'{nome.title()}, seu salário terá um aumento de 10%, agora passará a receber R${salario+(salario*(10/100)):.2f}!')'''