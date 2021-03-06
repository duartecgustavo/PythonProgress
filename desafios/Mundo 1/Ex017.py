# Desafio 17 - Aula 8 : Programa que leia o comprimento do cateto oposto e do catedo adjacente de um triangulo retangulo. # Depois calcule e mostre o comprimento da hipotenusa.

import math

coposto = float(input('Vamos calcular uma \033[31mhipotenusa\033[m de um \033[4:32mtriangulo retangulo\033[m.\nDigite o valor do \033[4:32mCateto Oposto\033[m: '))
cadjacente = float(input('Agora digite o valor do \033[4:32mCateto Adjacente\033[m: '))

hip = (coposto ** 2 + cadjacente ** 2) ** (1/2)
# calculo da hipotenusa, que é a soma dos qudrados dos catetos elevado a meio

print(f'O valor da \033[31mhipotenusa\033[m deste \033[4:32mtriângulo\033[m equivale à \033[34m{hip:.2f}\033[m!')

'''OUUU'''

hi = math.hypot(coposto, cadjacente)
# no python já existe o calculo da HIPOTENUSA pronto

print(f'O valor da \033[31mhipotenusa\033[m deste \033[4:32mtriângulo/033[m equivale à \033[34m{hi:.2f}\033[m!')
