# Desafio 46 - Aula 13 :Programa que mostre na tela um contagem regressiva de (1, 10) para o ano novo com intervalo de 1 segundo.

from time import sleep

for conta in range(10, 0, -1):
    print(conta)
    sleep(1)

print('\n\033[33mFELIZ ANO NOVO!!!\033[m')