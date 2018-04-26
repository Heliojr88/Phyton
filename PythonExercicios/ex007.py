# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nt1 = float(input('Digite a nota: '))
nt2 = float(input('Digite a outra nota: '))
md = (nt1 + nt2)/2
print('A média das notas são {:.1f}'.format(md))