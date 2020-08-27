# Desafio 96 - Aula 20: Programa que leia a LARGURA e ALTURA de um terreno e armazene em uma FUNÇÃO chamada área();
# Depois apresente a área do terreno.

def area(a , l):
    ar = a * l
    print(f'A área do terreno, seguindo a Largura de {l} e a Altura de {a} é igual à {ar}m²:')

a=(float(input('Altura: ')))
l=float(input('Largura: '))
area(a, l)
