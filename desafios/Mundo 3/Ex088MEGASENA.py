# Dessafio 88 - Aula 18 : MEGASENA - Programa que crie palpites.
# Primeiro deve pergutntar quantos jogos serão feitos.
# Depois para cada jogo sorteara 6 numeros entre 1 - 60 sendo que os numeros não podem se repetir dentro de um mesmo jogo.
# Deve cadastrar tudo em uma mesma lista composta.

from random import randint
from time import sleep

print('-='*25)
print(f'{"MEGASENA":^50}')
print('=-'*25)
print()
print('Valor do jogo - R$3,50\n')

quantjogos = []
count = 0

jogos = int(input('Quantos jogos deseja fazer? '))
valorjogo = jogos*3.50
for jogo in range(0, jogos):
    sorteionum = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    for valor in sorteionum:
        if sorteionum.count(valor) > 1:
            sorteionum = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60),
                          randint(1, 60)]
    sorteionum.sort()
    quantjogos.append(sorteionum[:])
    sorteionum.clear()

print('-='*25)
for jogo in quantjogos:
    count += 1
    print(f'Jogo {count} -',end=' ')
    for item in jogo:
        print(item,end=' ')
    print()
    sleep(0.75)

sleep(1)
print(f'\n{"Valor a pagar R$":^50}')
print(f'{valorjogo:^50.2f}')
print(f'\n{"BOA SORTE!":^50}')