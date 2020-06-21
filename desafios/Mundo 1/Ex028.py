# Desafio 28 - Aula 10 : Escreva um programa em que o programa escolhera um numero de 0 à 5 e depois peça ao usuario advinhar este numero.
# Caso o usuario acerte, ele granha o prêmio, se não ele não ganha nada!
from random import randint # ouuuu  from random inport randint
import time
lista = randint(0, 5)
print('-=-'*20)
print(f'{"BEM VINDO AO DESAFIO":=^60}')
print('-=-'*20)
usuario = float(input('Escolha um numero de \033[4m0 à 5\033[m!\nCaso você \033[34macerte\033[m podera realizar um desejo!\nQual será o numero? '))
print('\033[31mloading...\033[m')
time.sleep(3)
if usuario == lista:
    print('\033[32mMEUS PARABÉNS! VOCÊ ACERTOU O NUMERO DA SORTE, AGORA TCHAU!!!\033[m \033[31mVLW FLW!\033[m')
else:
    print(f'Definitivamente, não foi deste vez que você tirou a sorte grande, o numero correto é \033[34m{lista}\033[m.. tente novamente em outra vida!')