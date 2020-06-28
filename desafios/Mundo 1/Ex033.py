# Desafio 33 - Aula 10 : Programa que leia numeros e me indique qual é o Maior e qual é o Menor.

a = int(input('Digite o \033[4mprimeiro numero\033[m: '))
b = int(input('Digite o \033[4msegundo numero\033[m: '))
c = int(input('Digite o \033[4mterceiro numero\033[m :'))

lista = [a, b, c] # Numeros são guardados em um lista

print(f'O menor numero é \033[34m{min(lista)}\033[m e o maior é \033[34m{max(lista)}\033[m!')
# Comando Max e Min me indica quem é o maior e quem é o menor da lista

'''Código professor Guanabara: 
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
menor=a
if a>b and b<c:
    menor=b
if a>c and b>c:
    menor=c
maior=a
if a<b and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'O maior é {maior} e o menor é {menor}')'''