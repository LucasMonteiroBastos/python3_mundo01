#Exercício Python 26:
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

import math
frase = str(input('Escreva uma frase: ')).strip()
a = frase.upper()
print('A letra A aparece {} vez na frase'.format(a.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print(('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1)))