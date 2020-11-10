'''Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input('Informe um numero: '))
b = int(input('Informe um numero: '))
c = int(input('Informe um numero: '))

if a > b and a > c:
    print('(a) é maior {}'.format(a))
if b > c and b > a:
    print('(b) é maior {}'.format(b))
if c > a and c > b:
    print('(c) é maior {}'.format(c))
if a < b and a < c:
    print('(a) é menor {}'.format(a))
if b < c and b < a:
    print('(b) é menor {}'.format(b))
if c < a and c < b:
    print('(c) é menor {}'.format(c))
