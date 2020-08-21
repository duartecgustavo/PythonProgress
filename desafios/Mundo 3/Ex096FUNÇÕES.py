# Desafio 96 - Aula 20: Programa que leeia a LARGURA e ALTURA de um terreno e armazene em uma FUNÇÃO chmada area();
# Depois apresente a área do terreno.

def area(a , l):
    soma= a + l
    print(f'A área do terreno, seguindo a Largura de {l} e a Altura de {a} é iagual à {soma}:')


a=(float(input('Altura: ')))
l=float(input('Largura: '))
area(a, l)