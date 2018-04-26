# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de tarabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada

import random
al = 'João', 'Pedro', 'Gabriel', 'Maria', 'Ana', 'Pedro Gabriel', 'Lúcia', 'Hélio', 'Lucas', 'Júlio', 'Hudson'
enter = input('Aperte enter para escolher os alunos sorteados')
print('Os Alunos sorteados para a apresentação do trabalho serão os >>>> ', random.sample(al, 4))