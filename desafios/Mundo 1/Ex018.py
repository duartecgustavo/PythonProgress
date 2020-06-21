# Desafio 18 - Aula 8 : Faça um programa que leia um programa qualquer e calcule seu SENO, COSSENO E TANGENTE

import math
a = float(input('Digite um \033[4:32mangulo\033[m: '))
seno = math.sin(math.radians(a)) # math,radians é a necessidade de tranformar o numero digitado em um valor de angulo
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print (f'O \033[31mSENO\033[m de \033[32m{a:.0f}\033[m será \033[34m{seno:.2f}\033[m!')
print (f'O \033[31mCOSSENO\033[m de \033[32m{a:.0f}\033[m será \033[34m{cos:.2f}\033[m!')
print (f'A \033[31mTANGENTE\033[m de \033[32m{a:.0f}\033[m será \033[34m{tan:.2f}\033[m!')