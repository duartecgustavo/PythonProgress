# Desafio 104 - Aula 21: Programa que tenha a função leiaInt() que vai fazer a validação para aceitar apenas valores numericos.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            ok = True
            valor = int(numero)
        else:
            print('ERROO! Diga um numero inteiro valido!')
        if ok == True:
            break
    return valor 

# Programa principal
numero = leiaInt('Diga um numero: ')
print(f'O numero digitado foi {numero}.')
