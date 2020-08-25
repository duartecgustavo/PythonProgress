# Desafio 99 - Aula 20 : Programa que tenha a função maior() e que receba varios valores inteiros.
# Depois analise estesvalores e traga o maior.

def maior(*num):
    if len(num) == 0:
        print('-='*15)
        print(f'Analizando os valores passados...')
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor informado foi 0.')
    else:
        print('-='*15)
        print(f'Analizando os valores passados...')
        for c in num:
            print(c, end=' ')
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor informado foi {max(num)}.')

maior(5, 7, 9, 3, 2, 1)
maior(3, 6, 2, 22)
maior(2,3,5)
maior()
