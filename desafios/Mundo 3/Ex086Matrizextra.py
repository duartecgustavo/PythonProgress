# Desafio 86 - Aula 18 : Crie uma MATRIZ de dimensão 3x3 e preencha com valores do teclado.
# No final mostra na tela com a formatação correta.
# Versão Guanabara:

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Diga o valor da posição {linha, coluna}: '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')
    print()