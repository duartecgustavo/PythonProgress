# Dessafio 88 - Aula 18 : MEGASENA - Programa que crie palpites.
# Primeiro deve pergutntar quantos jogos serão feitos.
# Depois para cada jogo sorteara 6 numeros entre 1 - 60, sendo que os numeros não podem se repetir dentro de um mesmo jogo.
# Deve cadastrar tudo em uma mesma lista composta.

from random import randint

palpites=count=0
totpal=1
numeros=[]
banco=[]

palpites = int(input('Quantos paupites você deseja fazer? '))

while totpal <= palpites:
    while True:
        num = randint(1,60)
        if num not in numeros:
            numeros.append(num)
            count+=1
            print(numeros)
        if count ==6:
            break

    banco.append(numeros[:])
    numeros.clear()
    count=0
    totpal+=1
    

for pos, cont in enumerate(banco):
    print(f'{pos+1}° jogo: {sorted(cont)}.')