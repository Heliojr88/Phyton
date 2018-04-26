# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2

ht = float(input('Digite a altura da parede: '))
lg = float(input('Digite a largura da parede: '))
pr = ht * lg
tt = pr / 2
print('O metro quadrado da parede é {:.3} a quantidade de tinta necessária será de {} litros'.format(pr,tt))
