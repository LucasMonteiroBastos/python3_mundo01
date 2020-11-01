produto = float(input('Qual é o preço do produto? R$ '))
valor = produto * 5 / 100.0
result = produto - valor
print('O preço atual do produto é: R${:.2f} O preço do produto com  5% de desconto é: R${:.2f}'.format(produto,result))

