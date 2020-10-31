dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$: '))
dolar = dinheiro / 5.74
print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro,dolar))