# Desafio 113 - Aula 22 : Estrutura de funções que valide se o numero é inteiro ou float com módulo.

def leiaInt(msg):
    while True:
        try:
            inte = int(input(msg))
        except Exception:
            print('\033[31mERRO! Por favor digite um numero inteiro valido!\033[m')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario!')
            return 0
        else:
            return inte

def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except Exception:
            print('\033[31mERRO! Por favor digite um numero real valido!\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario!')
            return 0
        else:
            return real

num = leiaInt("Numero inteiro: ")
num2 = leiaFloat("Numero real: ")

print(f'O numero inteiro é {num} e o numero real é {num2}!')
