# Desafio 11 - Aula 07 : Leia os valores da altura e largura de uma parede, com base nisso calcule a área desta parede e a quantidade de tinta

# necessaria para pintar a parede toda, sabendo que cada Litro de tinta pinta 2m²
nome = input('\033[31mDigite seu nome aqui\033[m: ')
al = float(input('Digite a \033[33maltura\033[m da parede em m²: '))
l = float(input('Digite a \033[33mlargura\033[m da parede em m²: '))
ar = al*l
print('\033[31m{}\033[m, para pintar uma parede de \033[32m{}\033[mx\033[32m{}\033[m o que dá uma área total de \033[34m{:.1f}\033[mm², será necessario \033[32m{:.1f}\033[m litros de tinta!'.format(nome, al, l, ar, ar/2))