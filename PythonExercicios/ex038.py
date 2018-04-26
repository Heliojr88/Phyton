# Escreva uma programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = float(input('Digite o primeiro: '))
num2 = float(input('Digite o segundo: '))
if num1 > num2:
    print('O PRIMEIRO número é maior')
elif num2 > num1:
    print('O SEGUNDO é maior')
else:
    print('os DOIS são IGUAIS')
