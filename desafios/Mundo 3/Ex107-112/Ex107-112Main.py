import Modulos

salario = float(input('Informe seu salario: '))
aumento = int(input(f'Quantos % deseja aumentar no seu salario {salario}?'))
reajuste = int(input(f'Quantos % será reduzido em seu salario {salario}?'))

format = str(input(f'Quer formatar? [S/N]').upper()[0])
while format not in 'SN':
    format = str(input(f'Incorreto!\nQuer formatar? [S/N]').upper()[0])

if format in 'S':
    format=True
else:
    format=False

#moeda = str(input('Informe a moeda (R$, $): '))

print(f'A metade de seu salario de {salario} é {Modulos.metade(salario, format)}.')
print(f'O dobro de seu salario de {salario} é {Modulos.dobro(salario, format)}.')

print(f'Seu salario de {salario} teve um \033[35maumento de {aumento}%'
      f'\033[m. Agora você recebe \033[35m{Modulos.aumento(salario, aumento, format)}\033[m.')

print(f'Seu salario de R${salario} teve um \033[31mreajuste de {reajuste}%'
      f'\033[m. Agora você recebe \033[31m{Modulos.reajuste(salario, reajuste, format)}\033[m.')