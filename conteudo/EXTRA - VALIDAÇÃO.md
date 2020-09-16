# Estruturas de validação.

Por padrão eu uso o 'while not'

Exemplo:

choice = str(input('Quer continuar? [S/N]')).upper()[0]
while choice not in 'SN':
    choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]

Porém posso fazer uma validação de parâmetro mais refinada com comandos como 'isnumeric() ou isalpha()'

Exemplo: 

choice = str(input('Quer continuar? [S/N]')).upper()[0]
while choice not in 'SN' or choice.isalpha() == False:
    choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]