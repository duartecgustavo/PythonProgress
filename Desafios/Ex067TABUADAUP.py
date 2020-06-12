# Desafio 67 - Aula 15 : Programa que execute a tabuada de um numero digitado e pare quando for digitadou um numero negativo.

while True:
    num = int(input('Numero da Tabuada: '))
    if num < 0:
        break
    print('-'*50)
    for c in range(1,11):
        print(f'{num} * {c} = {num*c}')
    print('-'*50)
print('Fim do programa!')

# ouuu minha solução:

'''print('-'*50)
print(f'\033[32m{"TABUADA":^50}\033[m')
print('-'*50)
count = 0
num = int(input('O numero da tabuada: '))
while True:
    count +=1
    if num <= 0:
        break
    print(f'{num} x {count} = {num * count} ')
    if count == 10:
        num = int(input('O numero da tabuada: '))
        count = 0

print('Fim do programa.')'''''