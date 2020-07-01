# Desasfio 66 - Aula 15 : Programa que vá lendo numeros ate chegar na condição e parada que é 999. (usar BREAK)

count = soma = 0
while True: # cria uma repetição infinita
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    count+=1
    soma += numero
print(f'A soma dos {count} numeros digitados é igual à {soma}.')