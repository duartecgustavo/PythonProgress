# Desafio 25 - Aula 9 : Programa que leia um nome inteiro e diga se ela tem 'SILVA' no nome:

nome = (input('Digite seu \033[4mnome completo\033[m: ')).strip()
nome = nome.lower()

if nome.find('silva') == -1:
    print(f'O nome \033[34m{nome.title()}\033[m \033[31mNÃO\033[m possui \033[34m"SILVA"\033[m!')
else:
    print(f'O nome \033[34m{nome.title()}\033[m possui \033[32mSIM\033[m \033[34m"SILVA"\033[m!')

# ouuu

print('silva' in nome)