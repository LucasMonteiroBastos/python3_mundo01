'''Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem
E informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
Se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano = int(input('Ano de nascimento: '))

anoAtual = 2020

idade = 2020 - ano
faltaIdade = 18 - idade
dia = faltaIdade + anoAtual
alistamento = ano + 18

print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,anoAtual))
if idade > 18:
    print('Você ja deveria ter se alistado há {} anos.'.format(abs(faltaIdade)))
    print('Seu alistamento foi em {}'.format(alistamento))
elif idade == 18:
    print('Voce  esta na idade certa de se alistar.')
else:
    print('Ainda falta {} anos para se alistar'.format(faltaIdade))
    print('Seu alistamento será {}'.format(dia))