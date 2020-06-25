# Desafio 19 - Aula 8 : Programa que leia 4 nomes e sorteie apenas 1.

from random import randint
from random import choice

aluno1 = str(input('Digite o nome do \033[32mprimeiro aluno\033[m: '))
aluno2 = str(input('Digite o nome do \033[32msegundo aluno\033[m: '))
aluno3 = str(input('Digite o nome do \033[32mterceiro aluno\033[m: '))
aluno4 = str(input('Digite o nome do \033[32mquarto aluno\033[m: '))

lista = [aluno1,aluno2,aluno3,aluno4]
# lista com os valores pedidos

escolha = choice(lista)
# escolhendo apenas um valor com função choice

print(f"O \033[32maluno sorteado\033[m é o \033[34m{escolha}\033[m!")

# OUUU

alunos = tuple(str(input(f'O nome do {a+1}: ')) for a in range(0,4))
# com a função de TUPLA junto ao FOR, consigo realizar varias perguntas desta maneira

escolha2 = choice(alunos)

print(f"O \033[32maluno sorteado\033[m é o \033[34m{escolha2}\033[m!")
