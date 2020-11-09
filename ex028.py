'''Exercício Python 28:
Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

a = int(input('Em que numero estou pensando? '))

b = random.randint(0,5)

if a == b:
    print('Parabéns, você acerto! Você disse que pensei no número {} e  eu pensei no número {}.'.format(a,b))
else:
    print('Você errou, você disse eu pensei no número {}, mais na verdade eu pensei no número {}.'.format(a,b))