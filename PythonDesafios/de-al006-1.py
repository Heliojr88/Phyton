# Criar um programa que leia dois números e mostre a soma entre eles
n1 = float(input('Digite sua altura: '))
n2 = float(input('Digite seu peso: '))
imc = n2 / (n1**2)
print('Sua altura é {} e seu peso é {}, seu imc é {}'.format(n1,n2,imc))
