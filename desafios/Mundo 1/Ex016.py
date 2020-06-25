# Desafio 16 - Aula 8 : Programa que leia um numero real (ex: 1,2341) e mostre na tela o numero inteiro

import math

nome = input("Olá, digite se nome: ")

numero = float(input("Agora vou pedir que digite um numero real \033[32m(Ex: 1,23424)\033[m: "))

print(f'\033[31m{nome}\033[m, o numero que digitou em sua forma inteira fica \033[32m{math.trunc(numero)}\033[m!')
# função math.trunc retira tudo que vem depois da virgula de um numero, tornando inteiro

'''OUU'''

print(f'\033[31m{nome}\033[m, o numero que digitou em sua forma inteira fica \033[32m{int(numero)}\033[m!')
# função int (inteiro)
