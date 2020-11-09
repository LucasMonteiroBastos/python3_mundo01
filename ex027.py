#Exercício Python 27:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.


nomeCompleto = str(input('Digite o nome completo de uma pessoa: ')).strip()

nome = nomeCompleto.split()
print('Muito prazer em te conhecer {}'.format(nomeCompleto))
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[-1]))
