from random import shuffle
import random

print('>>>:x: :x: :x: :x: JOGO DA VERDADE OU DESAFIO :x: :x: :x: :x:<<<')
v1 = 'Você gosta de batata frita?'
v2 = 'Você gosta de correr?'
v3 = 'Você gosta de cachaça?'
v4 = 'Você gosta alguém?'
v5 = 'Você acredita em Deus?'
v6 = 'Você gosta de buceta?'
v7 = 'Você gosta de piroca?'
v8 = 'Você usa dorgas?'

d1 = 'Beije alguém a sua escolha?'
d2 = 'Use cocaina'
d3 = 'De 27 voltas de 1km'
d4 = 'Passe pimenta no seu pau'
d5 = 'Vire uma garrafa de balalaika'
d6 = 'De um socão na parede'
d7 = 'Rasque dinheiro'
d8 = 'Quebre um bolsominion no soco'

dv = [v1, v2, v3, v4, v5, v6, v7, v8]
random.shuffle(dv)
dd = [d1, d2, d3, d4, d5, d6, d7, d8]
random.shuffle(dd)

resp = (input('Digite "VERDADE" ou "DESAFIO" : ')).upper()[0]

if resp == 'V':
    print(dv[0])
else:
    print(dd[0])