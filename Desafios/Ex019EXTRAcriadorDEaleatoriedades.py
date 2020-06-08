import random

aleatorio = input('Digite algo que você \033[35mdeseja muito\033[m: ')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = random.choice(lista)
print (f'Sua chance de conquistar \033[35m{aleatorio}\033[m isto é de \033[31m{escolha}\033[m!')