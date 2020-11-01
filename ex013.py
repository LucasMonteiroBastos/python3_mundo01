salario = float(input('Informe o salario do funcionario: R$ '))
reajuste = salario + (salario * 15 / 100)

print('Um funcionario que ganhva R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salario,reajuste))