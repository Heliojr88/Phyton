# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de tarabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada
from random import shuffle
p1 = str(input('Digite o nome: '))
p2 = str(input('Digite o nome: '))
p3 = str(input('Digite o nome: '))
p4 = str(input('Digite o nome: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem da apresentação será')
print(lista)