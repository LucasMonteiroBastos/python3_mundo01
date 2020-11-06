#Exercício Python 19:
#Um professor quer sortear um dos seus quatro alunos
#para apagar o quadro.
#Faça um programa que ajude ele,
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#importando o modulo random
import random

#variaveis com os 4 alunos
aluno1 = str(input('Digite o nome do primeiro Aluno: '))
aluno2 = str(input('Digite o nome do segundo Aluno: '))
aluno3 = str(input('Digite o nome do terceiro Aluno: '))
aluno4 = str(input('Digite o nome do quarto Aluno: '))

#lista para receber as variaveis "alunos"
lista  = [aluno1,aluno2,aluno3,aluno4]

#escolhido recebe randomicamente uma variavel selecionada dentro da lista
escolhido = random.choice(lista)


#imprimindo o aluno selecionado de forma aleatoria
print('O aluno escolhido foi o(a) {}'.format(escolhido))

