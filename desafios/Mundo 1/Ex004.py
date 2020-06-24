# Desafio 4 - Aula 6 : Ler o tipo primitivo daquilo que foi digitado e dizer todas as infos pertinentes.

a = input('Digite algo: ')

print('\033[31mO tipo primitivo de {} é: '.format(a), type(a))
print('\033[32m{} é um numero?'.format(a), a.isnumeric())
print('\033[33m{} é alfabético?'.format(a), a.isalpha())
print('\033[34m{} possui espaços?'.format(a), a.isspace())
print('\033[35m{} está em alphanumerico?'.format(a), a.isalnum())
print('\033[36m{} está em maiusculo?'.format(a), a.isupper())
print('\033[37m{} esta em minusculo?'.format(a), a.islower())
print('{} esta capitalizada?'.format(a), a.istitle()) # nem maiuscula e nem minuscula