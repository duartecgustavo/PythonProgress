# Desafio 10 - Aula 07 : Com base na cotação do dolar atual, crie um programa que leia valor em R$ e de o valor em $$.

print('-='*25)
print(f'{"CONVERSOR DE MOEDA":^50}')
print('=-'*25)

nome = input ('\033[31mDigite seu nome ao lado\033[m: ')

valor = float(input('Agora digite o \033[33mvalor\033[m que você quer \033[35mconvertido\033[m em \033[31mdolar\033[m, \033[34m{}\033[m: '.format(nome)))

cotacao = float(input('Digite o \033[33mvalor\033[m da cotação atual do \033[31mdolar\033[m - U$$: '))

print('\033[34m{}\033[m, o \033[33mvalor\033[m de \033[31mR${:.2f}\033[m em \033[31mdolar\033[m é igual à \033[32mU$${:.2f}\033[m!'.format(nome, valor, valor/cotacao))
