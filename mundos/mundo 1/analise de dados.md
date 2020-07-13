#Ma nipulando  Cadeias de caracteres ou Strings (cada letra, espaço e caracter recebe um numero dentro do Python

# 1² FATIAMENTO
frase = '     Curso em Video Python      '
print (frase[9]) # Conchetes [] aciona o modo LISTA, que transforma o que foi digitado em uma lista de caracteres numerando eles de forma crescente
print (frase[9:13]) # Neste caso além de me mostra a letra na posição 9 'V' ele vai me trazer tudo até a letra 12 'e', a 13 não entra, é sempre um para trás)
print (frase[9:21])

print (frase[9:21:2]) # Agora, por conta do '2' ele vai pular as escolas a cada 1 digito (vai pular dois caracteres)
print (frase[:5]) # Começara no '0' pois não tem nada e terminara cno '5', mesma coisa que [0:5], aparecer 'curso'
print (frase[15:]) # Quase a mesma coisa, vai até o ultimo caracter
print (frase[9::3]) # Neste caso, depois da primeira : ele vai entender que deve r até o fim da frase digitada e a segunda vai indicar que é apra pular de 3 em 3

teste = input('Digite uma frase')
print (teste[2:])

# 2² ANALISE
# Vamos começar usando a função LEN, que vai ter quantos caracteres tem minha frase
print (len(frase))
print (len(frase.strip()))
print (len(teste))

# Outra função será o COUNT que irá contar tudo oque eu quiser dentro de uma frase
print (frase.count('o'))
print (frase.count('o',0,13)) # Vai me mostrar o numero de 'o' presente do caracter 0 até o 12 (lembrando que é sempre até um caracter anterior
print (teste.count('mundo'))

# Também temos o FIND, que vai procurar quantas vezes o caracter que eu quero apareceram
print (frase.find('deo')) # Caso eu indique um valor que não tem, ele irá me retonrar '-1', pois não existe nada correespondente
print ('curso' in frase)

# 3° TRANSFORMAÇAO
# Agora vamos aprender a transformar estes caracteres
print (frase.replace('python', 'android'))# REPLACE faz essa função
print (teste.replace('mundo', 'gerudo'))

print (teste.upper()) # UPPER deixa tudo maiusculo
print (frase.upper())

print (teste.lower()) # LOWER deixa tudo minusculo
print (frase.lower())

print (frase.capitalize()) # CAPITALIZE deixa a inicial maiusculas (do começo da frase)
print (frase.title()) # TITLE deixa TODAS as iniciais maiusculas

print (frase.strip()) # STRIP Vai retirar ESPAÇOS inultei de um frase (espaços que podem ser colocardos no começo e no fim
print (frase.rstrip()) # RSTRIP (RIGHT) remove os espaços da dereita
print (frase.lstrip()) # LSTRIP (LEFT) remove os espaços da esquerda

# 4° DIVISÃO e JUNÇÃO
# Com o comando SPLIT podemos dividir uma frase em quantas quisermos através dos espaços e com JOIN podemos unir frases
print (frase.split())
print (' '.join(frase))

print("""EXTRAAAA EXTRAAAAA, se eu quiser adicionar um texto, frase ou
qualquer coisa, e quero add em linhas diferentes, 3 
" juntas mes permitem abrir isso, sem precisar de \+n ou outro print'""")

# EXTRA - Para finalizar, no Python podemos adicionar comando a comandos, EX

print (frase.upper().count('A'))

mundo = 'Olá Mundo'
mundo = (mundo.replace('Mundo', 'world'))

    print (mundo)

dividido = (mundo.split())
print(dividido[0])
print(dividido[0][2])
