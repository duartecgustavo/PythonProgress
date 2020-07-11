# Desafio 85 - Aula 18 : Programa que leia 7 valores digitados pelo usuario e cadastre-os em uma lista unica.
# Esta lista deve manter os valores separados entre impares e pares e no final mostre os valores em ordem crescente.

valores = [[],[]]

for cont in range(1,8):
    valor = int(input(f'Diga o {cont}° valor: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print('=-'*30)
print(f'Os valores pares digitados foram: {valores[0]}.')
print(f'Os valores impares digitados foram: {valores[1]}.')