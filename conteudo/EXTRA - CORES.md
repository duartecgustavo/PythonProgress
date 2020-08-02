#### EXTRA - ADICIONANDO CORES :paintbrush:
> sempre que você quiser representar uma cor em Python, basta usar o comando para

* **ABRIR** - `\033+[styletext:collor:background+m`

* **FECHAR** - `\033[m`

**Exemplo:**

`print('\033[1:31:42m Olá, mundo!\033[m')`

> primeiro vem o **parâmetro** para **estilo** depois o de **cor**.

---
### Style - Estilos :registered:

\033+[**styletext**:collor:background+m

* **0** = Texto sem formatação -print('**\033[0m** Olá, mundo!**\033[m**')

* **1** = Negrito - print('**\033[1:30:41m** Olá, mundo!**\033[m'**)`

* **4** = Texto sublinhado - print('**\033[4:33:46m** Olá, mundo!**\033[m**')

* **7** = Inversão de cores com o fundo - print('**\033[7:35:43m** Olá, mundo!**\033[m**')

---
### Collors - Cor do texto :eight_spoked_asterisk:

\033+[styletext:**collor**:background+m

* 30 - Branco :white_circle:

* 31 - Vermelho :red_circle:

* 32 - Verde :green_circle:

* 33 - Amarelo :yellow_circle:

* 34 - Azul :large_blue_circle:

* 35 - Lilas :purple_circle:

* 36 - Azul BB :radio_button:

* 37 - Cinza :black_square_button: *cor padrão do terminal*

---
### Background - Cor do fundo :white_square_button:
> a mesma sequencia de cores do **collor**, mas com *40, 41, 42... 47* para o fundo

\033+[styletext:collor:**background**+m

---

### LISTA DE CORES :art:

```
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'lilas':'\033[35m'}
```

`nome = input('Digite seu nome ao lado: ')`

`print(f'Olá {cores["azul"]}{nome}{cores["limpa"]}, como vai seu {cores["vermelho"]}coração?{cores["limpa"]}')`


[:arrow_backward:](https://github.com/duartecgustavo/Python-Progress/blob/master/conteudo/indice.md)
