# Desafio 24 - Programa que leia o nome de uma cidade e mediga se começa ou não com a palavra 'SANTO'
cidade = input('Digite o nome da sua \033[4mcidade\033[m : ')

cidade = cidade.lower()
if 'santo' in cidade:
    print (f'A cidade \033[32m{cidade.title()}\033[m possui \033[32mSIM\033[m \033[34m"SANTO"\033[m no nome!')
else:
    print (f'A cidade \033[32m{cidade.title()}\033[m \033[31mNÃO\033[m possui \033[34m"SANTO"\033[m no nome!')

# ouuuu
print (cidade[:5] == "santo" )






