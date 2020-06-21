# Desafio 56 EXTRA - Aula 13 : Programa que leia o NOME, IDADE  e SEXO de 4 PESSOAS  e mediga:
# A MÉDIA DE IDADE do grupo.
# O NOME do HOMEM mais VELHO.
# Quantas MULHERES tem MENOS DE 20 ANOS.

plussage = 0

oldman = ''
oldageman = 0

youngwoman = 0

for c in range(1, 5):
    print(f'------------ {c}° pessoa ------------')
    nome = str(input(f'\033[32mNome\033[m: ')).lower()
    sexo = str(input(f'\033[32mSexo\033[m: ')).lower()
    age = int(input(f'\033[32mIdade\033[m: '))

    plussage += age

    if sexo in 'Mm' and c == 1:
        oldageman = age
        oldman = nome
    if sexo in 'Mm' and age > oldageman:
        oldageman = age
        oldman = nome

    if sexo in 'Ff' and age <=20:
        youngwoman += 1

print(f'A média de idade deste grupo é de {plussage/4} anos!')

print(f'O nome do homem mais velho é {oldman.capitalize()} e tem {oldageman} anos.')

print(f'O numero de mulheres com menos de 20 anos é igual à {youngwoman}.')