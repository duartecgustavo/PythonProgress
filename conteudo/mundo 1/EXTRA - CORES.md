#### EXTRA - ADICIONANDO CORES :paintbrush:
sempre que você quiser representar uma cor em Pythonbasta usar o comando `\033+[stylo:.text:.background+m`

**Ex:**

`print('\033[1:30:41m Olá, mundo!\033[m')`

`print('\033[4:33:46m Olá, mundo!\033[m')`

`print('\033[7:35:43m Olá, mundo!\033[m')`

`print('\033[30:42m Olá, mundo!\033[m')`

`print('\033[m Olá, mundo!\033[m')`

`print('\033[7:30m Olá, mundo!\033[m')`

# Style - Estilo da cor
# 0 = Texto sem formatação
# 1 = Negrito
# 4 = Texto sublinhado
# 7 = Inversão de cores com o fundo

# Text - Cor do texto
# 30 - Branco ; 31 - Vermelho ; 32 - Verde ; 33 - Amarelo ; 34 - Azul ; 35 - Lilas ; 36 - Azul bb ; 37 - Cinza(ocor padrõ do terminal;

# Backgroun - Cor do fundo
# a mesma sequencia do Text, mas com 40, 41, 42... 47;

# POSSO CRIAR TAMBÉM UMA LISTA DE CORES!!!
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'lilas':'\033[35m'}
nome = input('Digite seu nome ao lado: ')
print(f'Olá {cores["azul"]}{nome}{cores["limpa"]}, como vai seu {cores["vermelho"]}coração?{cores["limpa"]}')
