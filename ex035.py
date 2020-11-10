#Exercício Python 35:
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('\033[1;31mPrimeiro segmento: '))
b = float(input('\033[1;33mSegunda segmento: '))
c = float(input('\033[1;35mTerceioro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[mOs segmentos acima podem forma um TRIANGULO!')
else:
    print('Os segmentos acima não formam um TRIANGULO!')

