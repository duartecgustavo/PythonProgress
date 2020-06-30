# Desafio 58 - Aula 14 : Melhorar o jogo do desafio 28.
# Computador vai pensar em um numero de 0 à 10. O jogador vai ir tentando advinhar, quando acertar o computador vai mostrar o numero de tentativas que o jogador levou até acertar.

from random import randint

# Escolha do computador
computador = randint(0,10)

# Escolha do usuario
print('\033[32m-|\033[m'*50)
usuario = int(input(f'Sua escolha [1 até 10]:'))
tentativas = 1

while usuario != computador:
    if usuario > computador:
        print('MENOS')
    elif usuario < computador:
        print('MAIS')
    usuario = int(input('Eroooooou, tente novamente: '))
    tentativas +=1

if tentativas == 1:
    print('PARABÉNS! Dê PRIMEIRA VIDENTE DO CARAIO')
else:
    print(f'Aleluiaaaaa, o numero escolhido pelo PC foi\n{computador}\nVocê fez {tentativas} apostas.')