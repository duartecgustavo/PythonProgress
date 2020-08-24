# Desafio 97 - Aula 20: Receba um texto qualquer como parametrô e mostre a mensagem de forma adaptavel:

def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)

for count in range(0,3):
    escreva(msg = str(input('Escreva uma mensagem: ')))