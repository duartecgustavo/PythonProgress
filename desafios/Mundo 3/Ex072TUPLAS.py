# Desafio 72 - Aula 16 : Programa que leia uma TUPLAS que vá de 0 à 20 por EXTENSO;
# Depois o programa irá perguntar um numero entre 0 e 20 e mostra-lo por extenso;

lista = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez','onze','doze','treze','catorze','quinze','dezesseis','deszessete','dezoito','dezenove','vinte')

print('-'*50)
print(f'{"LEITOR DE NUMEROS POR EXTENSO": ^50}')
print('-'*50)

while True:
    user = int(input('\nMe diga um numero entre (\033[34m0 e 20\033[m):' ))
    while user > 20 or user < 0:
        user = int(input('\033[31mValor invalido!\033[m\nDiga um numero entre (\033[34m0 e 20\033[m): '))

    print('-'*50)
    print(f'O numero {user} em extenso é igual à \033[32m{lista[user].capitalize()}\033[m!')

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m\nQuer continuar? ')).upper()[0]

    if choice in 'N':
        break

print('\033[33mPrograma finalizado!')