# BIBLIOTECAS : Começando pela MATH, com essa biblioteca posso executar NOVOS comandos matematicos, posso importala INTEIRA (IMPORT MATH) ou
# importala por determinada função ESPECIFICA exemplo, (FROM MATH IMPORT SQRT)
import math  # importei a biblioteca toda
from datetime import date

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)  # SQRT é o comando para raiz quardada
print(f'A raiz quadrada de {num} é iguaç à: {raiz:.1f}')
print(f'A raiz quadrada de {num} é igual à: {math.ceil(raiz)}!')  # CEIL é o comando para arredondar para cima
print(f'A raiz quadrade de {num} é igual à: {math.floor(raiz)}!')  # FLOOR arredonda para baixo
print(f'A raiz quadrada de {num} é igual à: {math.trunc(raiz)}!')  # TRUNC tudo que estiver da virgula para direita do numero será eliminado

# -----------------------------// ---------------------// -------------------------

import emoji
print(emoji.emojize("Olá, mundo! :earth_americas:", use_aliazes=True))

# # -----------------------------// ---------------------// -------------------------

import random
print('ATENÇÃO - Sorteio de quem enfiara uma bigorna no cú do Bolsonaro')
n1 = input('Digite o nome do primeiro candidato: ')
n2 = input('Digite o nome do segundo candidato: ')
n3 = input('Digite o nome do terceiro candidato: ')
n4 = input('Digite o nome do quarto candidato: ')
lista = [n1,n2,n3,n4]
sor = random.choice(lista)
print(f"O candidato contemplado é {sor}, meus PARABÉNS!")

#from time import sleep
#from termcolor import colored
#from date time date
