 # Desafio 35 - Aula 10 : Programa que leia 3 retas e me diga se podem ou não formarem um triângulo.

print (f'\033[32m{" VAMOS MONTAR UM TRIANGULÔ! ":=^50}\033[m')

a = int(input(f'{"Digite a primeira medida: "}'))
b = int(input(f'{"Digite a segunda medida: "}'))
c = int(input(f'{"Digite a terceira medida: "}'))

# As retas podem formar um triangulo, caso a soma de duas delas não sejam iguais ou maiores que a terceira.
if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print(f'Aqui temos um triangulo, \033[34mparabéns\033[m!')
else:
    print(f"\033[31mInfelismente não se formou um triangulo!\033[m")