# Desafio 70 - Aula 15 : Programa que leia o NOME e o PREÇO de varios produtos e pergunte se quer continuar.
# A/ Qual o total gasto na compra.
# B/ Quantos produtos custam mais de R$1000.
# C/ Qual o nome do produto mais barato.

print('-='*25)
print(f'\033[32m{"LEITOR DE PRODUTOS":^50}\033[m')
print('=-'*25)

tot = tot1000 = menor = count = 0
namemenor = ' '

while True:
    print('\033[31m-=\033[m' * 25)
    print(f'{"PRODUTO":^50}')
    count +=1

    name = str(input('Nome do produto: ')).lower()
    price = float(input('Preço do produto: R$'))

    tot +=price
    # total gasto

    if price > 1000:
        tot1000 +=1
    # produtos mais de R$1000

    if count == 1 or price < menor:
        menor = price
        namemenor = name
    # produto mais barato

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m Quer continuar?[S/N] ')).upper()[0]

    if choice in 'N':
        print('Finalizando programa!.. ')
        break

print('-='*25)
print(f'Total gasto: \033[34mR${tot:.2f}\033[m.')
print(f'No total {tot1000} produtos custaram mais de \033[31mR$1000.00\033[m.')
print(f'O produto mais barato foi o \033[34m{namemenor}\033[m que custou apenas \033[32mR${menor:.2f}\033[m.')