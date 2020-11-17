'''Exercício Python 42:
Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''



a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a == b and a == c and b == c:
    print('Os segmentos formam um triangulo EQUILÁTERO.')
elif a == b and a != c and b != c and a != b and a != c and b == c:
    print('Os segmentos formam um triangulo ISÓSCELES.')
elif a != b and a != c and b != c:
    print('Os segmentos formam um triangulo ESCALENO.')