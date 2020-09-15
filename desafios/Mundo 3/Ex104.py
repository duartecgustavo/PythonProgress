# Desafio 104 - Aula 21: Programa que tenha a  função leiaInt(), que vai fazer a validação para aceirtar  apeenas valores numericos.

def leiaInt(num):

    while True:
        if num.isnumeric():
            return num
            break
        else:
            num = str(input('Digite um numero valido: '))


# Programa Principal

numero = str(input('Diga um numero: '))
print(f'O numero digitado foi {leiaInt(numero)}.')
