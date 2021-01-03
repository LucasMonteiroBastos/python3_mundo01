import random
print('Quais Opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogada = int(input('Qual a sua jogada? '))
computador = random.randrange(3)
print('')


print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
if computador == 0:
    print('Computador jogou PEDRA')
elif computador == 1:
    print('Computador jogou PAPEL')
elif computador == 2:
    print('Computador jogou TESOURA')

if jogada == 0:
        print('Humano jogou PEDRA')
elif jogada == 1:
        print('Humano jogou PAPEL')
elif jogada == 2:
        print('Humano jogou TESOURA')

if jogada == 0 and computador == 1:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('Computador GANHOU!')
elif jogada == 0 and computador == 2:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('Humano GANHOU!')
elif jogada == 0 and computador == 0:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('EMPATE')

if jogada == 1 and computador == 0:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('Humano GANHOU!')
elif jogada == 1 and computador == 2:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('COMPUTADOR GANHOU! ')
elif jogada == 1 and computador == 1:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('EMPATE')

if jogada == 2 and computador == 0:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('COMPUTADOR GANHOU!')
elif jogada == 2 and computador == 1:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('Humano GANHOU')
elif jogada == 2 and computador == 2:
    print('=-=-=-==-=--=--=-=-=-=-=-=-=-')
    print('EMPATE')







