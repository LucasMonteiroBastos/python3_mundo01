#Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.


a = int(input('Digite um número inteiro: '))
print('''Escolha uma das basis para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] convertar para HEXADECIMAL''')

opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('{} convertido em BINÁRIO é igual a \033[1;31m{}'.format(a, bin(a)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é igual a \033[1;31m{}'.format(a, oct(a)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igual a \033[1;31m{}'.format(a,hex(a)[2:]))
else:
    print('\033[1;31mOPÇÃO INVALIDA!\033[m Digite uma opção valida.')
