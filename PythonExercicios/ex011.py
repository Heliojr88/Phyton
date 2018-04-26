# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2

ht = float(input('Digite a altura da parede: '))
lg = float(input('Digite a largura da parede: '))
dmao = float(input('Quantas demão você vai fazer: '))
pr = ht * lg
soma = pr * dmao
tt = soma / 2
print('Sua parede tem a dimensão de {}x{}'.format(ht, lg))
print('O metro quadrado da parede é {:.2f}m² a quantidade de tinta necessária será de {} litros'.format(pr,tt))
