# Escreva uma programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('Primeiro número é maior')
elif n2 > n1:
    print('Segundo número é maior')
else:
    print('O dois números são iguais')