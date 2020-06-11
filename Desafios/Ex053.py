# Desadio 53 - Aula 13 : Programa que leia uma frase e me diga se ela é um palindromo ou não;

frase = input('Digite uma frase: ').lower()

palavras = frase.split()
juntar = ''.join(palavras)
invert = ''
for letras in range(len(juntar)-1, -1, -1):
    invert = invert + juntar[letras]
if juntar == invert:
    print('É um Plalimdromo')
else:
    print('Não é um Palimdromo')