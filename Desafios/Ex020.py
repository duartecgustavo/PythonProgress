# Desafio 20 - Aula 8 : Programa que leia o nome de quatro alunos, sorteie e mostre a ordemm de apresentação de cada um.

import random
n1 = (input('Digite o nome do \033[32mprimeiro aluno\033[m: '))
n2 = (input('Digite o nome do \033[32msegundo aluno\033[m: '))
n3 = (input('Digite o nome do \033[32mterceiro aluno\033[m: '))
n4 = (input('Digite o nome do \033[32mquarto aluno\033[m: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) # Comando ramdon.shuffle é usado para embaralhar coisas
print(f'A ordem de apresentação será em ordem crescente:\n \033[34m{lista}\033[m')

