#Exercício Python 34:
# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,
# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Informe o salario do funcionario: R$ '))

if salario > 1250.00:
    aumento = salario + (salario * 10) / 100
    print('O valor do salario foi atualizado com mais 10%. Ficando com valor de \033[1;33mR${:.2f}'.format(aumento))
if salario < 1250.00:
    aumento = salario + (salario * 15) / 100
    print('O valor do salario foi atualizado com mais 15%. Ficando com valor de \033[1;34mR${:.2f}'.format(aumento))