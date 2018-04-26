# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

from random import choice
p1 = str(input('Digite o nome do aluno: '))
p2 = str(input('Digite o nome do aluno: '))
p3 = str(input('Digite o nome do aluno: '))
p4 = str(input('Digite o nome do aluno: '))
pt = [p1, p2, p3, p4]
es = choice(pt)
print('O aluno escolhido foi {}'.format(es))