# Desafio 12 - Aula 07 : Programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

nome = input('\033[31mOlá, digite seu nome ao lado\033[m: ')

preco = float(input('Digite o preço do produto, R$'))
precodesconto = preco - (preco * (5 / 100))

print(f'\033[34m{nome}\033[m, o valor do produto com \033[4:32m5% de desconto\033[m é igual à \033[31mR${precodesconto:.2f}\033[m!')