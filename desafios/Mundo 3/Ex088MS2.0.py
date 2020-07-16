# Dessafio 88 - Aula 18 : MEGASENA - Programa que crie palpites.
# Primeiro deve pergutntar quantos jogos serão feitos.
# Depois para cada jogo sorteara 6 numeros entre 1 - 60 sendo que os numeros não podem se repetir dentro de um mesmo jogo.
# Deve cadastrar tudo em uma mesma lista composta.
# versão guanabara

from random import randint

lista = []
jogos = []
count = 0
totjogos = 1

print('-='*25)
print(f'{"MEGASENA":^50}')
print('=-'*25)
print()

quant = int(input('Quantos jogos você deseja fazer? '))
while totjogos <= quant:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            count+=1
        if count == 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totjogos+=1
    count=0

print('=-'*25)

for pos, jogo in enumerate (jogos):
    print(f'Jogo {pos+1} - ',end=' ')
    print(jogo)