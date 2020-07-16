# Desafio 87 - Aula 18 : Melhorar o desafio 86, mostrando no final:
# A/ A SOMA de todos os valores PARES digitados
# B/ A SOMA de todos os valores da TERCEIRA COLUNA.
# C/ O MAIOR valor da SEGUNDA COLUNA.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

somapar = somatercol = maiorseg = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input('Diga um numero: '))


for linha in range(0,3):
    print(f'Linha {linha+1} - ',end=' ')
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')

        # soma pares
        if matriz[linha][coluna] % 2 == 0:
            somapar+=matriz[linha][coluna]
        #soma 3°coluna
        if coluna == 2:
            somatercol+=matriz[linha][coluna]
        # maior valor 2°coluna
        if linha == 1:
            if matriz[linha][coluna] == 0 or matriz[linha][coluna] > maiorseg:
                maiorseg = matriz[linha][coluna]


    print()

print(f'A soma dos valores pares da Matriz é igual à {somapar}')
print(f'\nA soma dos valores da 3° coluna da Matriz é igual à {somatercol}')
print(f'\nO maior valor da 2° linha é igual à {maiorseg}')


