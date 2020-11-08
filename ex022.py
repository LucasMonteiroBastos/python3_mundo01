'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em maiúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} caracteres.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))