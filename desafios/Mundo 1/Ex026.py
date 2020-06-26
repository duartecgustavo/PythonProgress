# Desafio 26 - Aula 9 : Programa que leia uma frase e me diga:
# 1 - Quantas vezes aparece a letra A.
# 2 - Em que posição ela aparece na primeira vez.
# 3 - Em que posição ela aparece na ultima vez.

frase = str(input('Digite uma frase : ')).lower().strip()

# 1
print (f'Na frase \033[32m"{frase.title()}"\033[m a letra \033[34m"A"\033[m se repete \033[31m{frase.count("a")} vezes\033[m.')

# 2
print (f'Na frase \033[32m"{frase.title()}"\033[m a letra \033[34m"A"\033[m apareceu na posição \033[31m{frase.find("a")+1}\033[m!')

# 3
print (f'Na frase \033[32m"{frase.title()}"\033[m a ultima letra \033[34m"A"\033[m aparece na posição \033[31m{frase.rfind("a")+1 }\033[m!')

# EXTRA - Colocar a frase ao contrario
contrario = frase[::-1]
print (f'A frase \033[32m"{frase.title()}"\033[m invertida fica : \033[34m{contrario}\033[m!')