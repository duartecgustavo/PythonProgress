# Desafio 38 - Aula 12 : Programa que leia 2 numeros inteiros, compare-os e mostre:
# Se o primeiro valor é maior / Se o segundo valor é maior / Se os valores são iguais

numero = int(input('Digite um numero: '))
numero2 = int(input('Agora digite outro numero: '))

if numero > numero2:
    print('O \033[34mprimeiro valor\033[m é MAIOR!')
elif numero2 > numero:
    print('O \033[34msegundo valor\033[m é MAIOR!')
else:
    print('Os valores são \033[32mexatamente IGUAIS\033[m!')