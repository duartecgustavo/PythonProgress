# Desafio 69 - Aula 15 : Programa que leia a IDADE, SEXO de varias pessoas e me pergunte se o usuario deseja continuar.
# Ao fim mostre:
# A/ Quantas pessoas tem  mais de 18 anos.
# B/ Quantos homens foram cadastrados.
# C/ Quantas mulheres tem menos de 20 anos.

age = countage = countman = countwoman = 0
sex = choice = ' '

while True:

    print('=-' * 25)
    print(f'{"CADASTRO DE PESSOAS!":^50}')
    print('-=' * 25)

    age = int(input('Sua idade: '))
    sex = str(input('Seu sexo[H/M]: ')).upper()
    while sex not in 'HM':
        sex = str(input('Opção invalida! Seu sexo[H/M]: ')).upper()

    if age > 18:
        countage += 1
    if sex in 'H':
        countman+=1
    if age < 20 and sex in 'M':
        countwoman+=1

    choice = str(input('Quer continuar?[S/N] ')).upper()
    while choice not in 'SN':
        choice = str(input('Opção invalida! Quer continuar?[S/N] ')).upper()
    if choice in 'N':
        break

print('-='*25)
print(f'{"DADOS!":^50}')

print(f'Pessoas maiores de idade: {countage}')
print(f'Homens: {countman}')
print(f'Mulheres menores que 20 anos: {countwoman}')
