'''Exercício Python 44:
Elabore um programa que calcule o valor a ser pago por um produto,
Considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

valor = float(input('Informe o valor do produto R$:'))
print('Informe a forma de pagamento: 1 para (– à vista dinheiro/cheque: 10% de desconto)')
print('Informe a forma de pagamento: 2 para (– à vista no cartão: 5% de desconto)')
print('Informe a forma de pagamento: 3 para (– em até 2x no cartão: preço formal)')
print('Informe a forma de pagamento: 4 para (– 3x ou mais no cartão: 20% de juros)')

pagamento = float(input('Forma de Pagamento: '))
if(pagamento == 1):
    a = valor - (valor * 10 / 100)
    print('Valor com 10% de desconto R$:{:.2f}'.format(a))
if(pagamento == 2):
    b = valor - (valor * 5 / 100)
    print('Valor com 5% de desconto R$:{:.2f}'.format(b))
if(pagamento == 3):
    print('Valor com preço normal. R$:{:.2f}'.format(valor))
if(pagamento == 4):
    c = valor + (valor * 20 / 100)
    print('Valor com 20% de juros R$:{:.2f}'.format(c))