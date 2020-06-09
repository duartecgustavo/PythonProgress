# Desafio 23 - Programa que leia qualquer numero entre 0 e 9999 e monstre na tela cada um dos digitos separados. Exemplo:
# Numero: 1834 --> Unidade 4 / Dezena 3 / Centena 8 / Milhar 1

numero = int(input('Digite um numero \033[4maté 9999\033[m : ')) # usaremos os comandos // resto de divisão e % produto da divisão
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'\033[31mUnidade : {u}\n\033[32mDecimal : {d}\n\033[33mCentena : {c}\n\033[34mMilhar  : {m}')

'''Cara, eu peguei um papel e fiz as contas e consegui entender. Não sei se você ainda tem dúvida, mas vou tentar explicar(sou péssimo explicando):
Usaremos o número 1957 para fazer as contas... Este código que o Guanabara usou, poderia ser simplificado para isto(O resultado vai ser o mesmo, pode testar):
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000

u recebe o resto da divisão inteira entre 1957 e 10 -->      1957 // 10 = 195 (10x195 = 1950), o resto dessa divisão é 7, logo, a unidade é 7. 
d recebe o resultado da divisão inteira entre 1957 e 10, esse resultado vai ser dividido por 10 novamente e pegará o resto dessa divisão, ficando assim:       1957 / 10 = 195(neste caso é o resultado da divisão inteira, não o resto) --> dividindo esse resultado por 10:   195 // 10 = 19 (19x10 = 190). Agora sim pegaremos o resto da divisão, que é 5. Logo, a dezena e 5.
c = Aqui é o mesmo processo anterior, só que dividindo por 100 -->       1957 // 100 = 19(resultado da divisão inteira). Agora faremos 19 // 10 = 1 (O resto dessa divisão inteira é 9). A centena é 9.
m recebe o resultado da divisão inteira entre 1957 e 1000 -->    1957 / 1000 = 1 (pronto, 1 é o milhar).

Obs: Lembre-se que divisão inteira pega apenas a parte inteira do número, diferente da divisão "normal" que daria valores com vírgula. '''
