#### EXTRA - ADICIONANDO CORES :paintbrush:
> sempre que você quiser representar uma cor em Python, basta usar o comando `\033+[stylo:.text:.background+m`

**Exemplo:**

`print('\033[1:30:41m Olá, mundo!\033[m')`

`print('\033[4:33:46m Olá, mundo!\033[m')`

`print('\033[7:35:43m Olá, mundo!\033[m')`

`print('\033[30:42m Olá, mundo!\033[m')`

`print('\033[m Olá, mundo!\033[m')`

`print('\033[7:30m Olá, mundo!\033[m')`

> primeiro vem o **parâmetro** para **estilo** depois o de **cor**.

---

### Style - Estilos :registered:

* **0** = Texto sem formatação.

* **1** = Negrito.

* **4** = Texto sublinhado.

* **7** = Inversão de cores com o fundo.

---
### Collors - Cor do texto :eight_spoked_asterisk:

* 30 - Branco :white_circle:

* 31 - Vermelho :red_circle:

* 32 - Verde :green_circle:

* 33 - Amarelo :yellow_circle:

* 34 - Azul :large_blue_circle:

* 35 - Lilas :purple_circle:

* 36 - Azul BB :radio_button:

* 37 - Cinza :black_square_button: cor padrão do terminal

---

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
