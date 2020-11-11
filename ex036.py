#Exercício Python 36:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


valorCasa = float(input('Informe o valor da casa: R$'))

salário = float(input('Informe o salário do comprador: R$'))

quantosAnos = int(input('Em quantos anos voce ira pagar? '))


#resultados
anos = quantosAnos * 12
prestacao = valorCasa / anos

porcento = (salário * 30) / 100

print('O valor o Imovel é R$\033[1;32m{:.2f}\033[m e para pagar em \033[1;35m{}\033[m anos, a prestação será de R$\033[1;36m{:.2f}\033[m'.format(valorCasa,quantosAnos,prestacao))

if prestacao > porcento:
    print('Emprestimo NEGADO!')
else:
    print('\033[1;31mEMPRÉSTIMO ACEITO')


