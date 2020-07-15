### Manipulando cadeias de caracteres ou strings.
cada letra, espaço e numero digitado é transformado em uma lista no Python e possui sua posição

##### FATIAMENTO:

* Quando digitamos algo, exemplo uma frase, podemos fatiar usando comandos simples como `[]`. Eles acionam o **modo LISTA**, assim a frase se tonra uma lista que sempre **começa em 0**.

`frase = '     Fora Bolsonaro!      '` - apenas uma frase aleatoria

`print (frase[9])` - Aqui estamos pedindo o *caracter* na **posição 9**.

`print (frase[9:13])` - Com o uso das :, além de mostrar a **posição 9**, irá mostrar até a **posição 12**, sempre ignora o ultimo.

`print (frase[9:21:2])` - Por conta do **'2' no ultimo parametro** ,irá mostrar os caracteres no espaço delimitado **pulando dois**.

`print (frase[:5])` - **Começara no '0'** pois **não tem parametro** de começo e **terminara no '4'**.

`print (frase[15:])` - Possui parametro de começo, mas não de final, então **vai até o ultimo**.

`print (frase[9::3])` - Possui parametro de começo, mas não de final, vai até o ultimo **pulando de três em três**.

* Com `INPUT` funciona igual. **Ex:**

`frase = input('Digite uma frase')`

`print (frase[2:])`

---
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
