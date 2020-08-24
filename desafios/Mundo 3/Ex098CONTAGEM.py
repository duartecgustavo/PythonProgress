# Desafio 98 - Aula 20: Programa que tenha uma função contador() e que receba 3 parâmetros: Inicio, Fim e Passo.
# Então esta função deve realizar 3 contagens 
# A/ De 1 até 10, de 1 em 1
# B/ De 10 até 0, de 2 em 2
# C/ E uma contagem personalizada

from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1 # tranforma o numero em positivo
    print('-='*15)
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if i < f:
        for count in range(i, f+p, p):
            print(count, end=' ', flush=True)
            sleep(0.3)
        print('FIM!')
    else:
        for count in range(i, f-p, -p):
            print(count, end=' ', flush=True)
            sleep(0.3)
        print('FIM!')                 

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de ditar a contagem: ')
contador(i = int(input('Inicio: ')), f = int(input('Fim: ')), p = int(input('Passo: ')))