choice = str(input('Quer continuar? [S/N]')).upper()[0]
while choice not in 'SN' or choice.isalpha() == False:
    choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]