# Desafio 18 - Aula 8 : Faça um programa que leia um angulo qualquer e calcule seu SENO, COSSENO E TANGENTE

import math

angulo = float(input('Digite um \033[4:32mangulo\033[m: '))

# no próprio python já possuem os calculos prontos para o SENO, COSSENO e TANGENTE
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
# math.radians é a necessidade de tranformar o numero digitado em um valor de angulo

print (f'O \033[31mSENO\033[m de \033[32m{angulo:.0f}\033[m será \033[34m{seno:.2f}\033[m!')
print (f'O \033[31mCOSSENO\033[m de \033[32m{angulo:.0f}\033[m será \033[34m{cos:.2f}\033[m!')
print (f'A \033[31mTANGENTE\033[m de \033[32m{angulo:.0f}\033[m será \033[34m{tan:.2f}\033[m!')