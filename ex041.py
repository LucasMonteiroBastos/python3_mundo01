'''Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''


nome = str(input('Informe sua nome: '))
anoNascimento = int(input('Informe sua data de nascimento: '))
ano = 2020
idade = ano - anoNascimento
print('{}, você nasceu em {}, portanto sua idade é de {} anos.'.format(nome,anoNascimento,idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade > 9 and idade <=14:
    print('Sua categoria é INFANTIL.')
elif idade >14 and idade <= 19:
    print('Sua caterogia é JÚNIOR.')
elif idade > 19 and idade <= 25:
    print('Sua caterogia é SÊNIOR.')
elif idade > 25:
    print('Sua caterogia é MASTER.')

