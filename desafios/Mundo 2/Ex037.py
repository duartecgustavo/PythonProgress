# Desafio 36 - Aula 12 : Conversor de bases, digite um numero e converta para Binario, Octal ou Hexadeciamal

num = int(input('Digite um numero: '))
print('Agora escolha uma forma de conversão:')

print('[ 1 ] - converter para BINARIO')
print('[ 2 ] - converter para OCTAL')
print('[ 3 ] - converter para HEXADECIAMAL')

escolha = int(input('Digite sua escolha: '))

# Já existem os comando setados para conversão
if escolha == 1:
    print(f'O numero {num} em BINARIO é igual à {bin(num)[2:]}') # Binario
elif escolha == 2:
    print(f'O numero {num} em OCTAL é igual à {oct(num)[2:]}') # Octal
elif escolha == 3:
    print(f'O numero {num} em HEXADECIMAL é igual à {hex(num)[2:]}') # Hexadecimal
else:
    print('Esta escolha é invalida!')