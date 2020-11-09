'''Exercício Python 31:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km.
E R$0,45 para viagens mais longas.'''

distancia = float(input('Distancia: '))

a = distancia * 0.45
b = distancia * 0.50

print('Voce irá fazer uma viagem de {} Km.'.format(distancia))

if distancia > 200:
    print('O valor a ser cobrado é de R${:.2f}'.format(a))
else:
    print('O valor a ser cobrado é de R${:.2f}'.format(b))