# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random
al = 'João', 'Pedro', 'Gabriel', 'Maria', 'Ana', 'Pedro Gabriel', 'Lúcia', 'Hélio', 'Lucas'
enter = input('Aperte enter para escolher o aluno aleatório')
print('O aluno que irar apagar o quadro será ????? >>>>>  ', random.choice(al))