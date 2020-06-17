import random
print('\033[32m=\033[m'*50)
print(f'\033[34m{"OLÁ, VAMOS PRATICAR O DESAFIO DE HOJE!":^50}\033[m')
print('\033[32m=\033[m'*50)

n = input('Aperte \033[34mENTER\033[m para escolher um \033[31mdesafio\033[m.')

rand = random.randint(1, 55)
print(f'O desafio escolhido de hoje é o \033[31m{rand}\033[m, refaça ele e releembre o conteúdo')
