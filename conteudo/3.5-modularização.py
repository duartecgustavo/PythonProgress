# Modularização - dividir o programa emm pedaços

# Exemplo: 

def fatorial (num):
    f=1
    for c in range(1, num+1):
        f*=c
        print(f)
    return f

num = int(input('Um numero: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}!')