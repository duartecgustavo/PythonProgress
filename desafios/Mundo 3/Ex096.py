# Desafio 97 - Aula 20: Receba um texto qualquer como parametrô e mostre a mensagem de forma adaptavel:

def escreva(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

for count in range(0,3):
    escreva(msg = str(input('Escreva uma mensagem: ')))