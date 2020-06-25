# Desafio 20 - Aula 8 : Programa que leia o nome de quatro alunos, sorteie e mostre a ordemm de apresentação de cada um.

import random

alunos = list(str(input('Diga seu nome: ')) for c in range(0,4))

random.shuffle(alunos) # comando ramdon.shuffle é usado para embaralhar listas

print(f'A ordem de apresentação será em ordem crescente:\n \033[34m{alunos}\033[m')

