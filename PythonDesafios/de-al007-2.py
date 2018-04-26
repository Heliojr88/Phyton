# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um número: '))
print('O dobro de {} é {}\no seu triplo é {}\nraiz quadrada é {:.2f}'.format(n1,(n1*2),(n1*3), pow(n1, (1/2))))
