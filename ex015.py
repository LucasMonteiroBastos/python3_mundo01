#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugado = int(input('Por quantos dias o veiculo foi alugado? '))
km = float(input('Qual a quantidade de Km percorrido? '))


preço = diasAlugado * 60 + km * 0.15

print('O total a pagar pelo aluguel do veiculo é: R${:.2f}'.format(preço))