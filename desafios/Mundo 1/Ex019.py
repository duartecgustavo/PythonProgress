# Desafio 19 - Aula 8 : Programa que leia 4 nomes e sorteie apenas 1.

import random

n1 = str(input('Digite o nome do \033[32mprimeiro aluno\033[m: '))
n2 = str(input('Digite o nome do \033[32msegundo aluno\033[m: '))
n3 = str(input('Digite o nome do \033[32mterceiro aluno\033[m: '))
n4 = str(input('Digite o nome do \033[32mquarto aluno\033[m: '))
lista = [n1, n2, n3, n4]
choice = random.choice(lista)
print(f"O \033[32maluno sorteado\033[m é o \033[34m{choice}\033[m!")
