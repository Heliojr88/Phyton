#Crie um o programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letra ao todo ( sem considerar espaços )
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Nome completo com letras MAIÚSCULAS >> {}'.format(nome.upper()))
print('Nome completo com letras minúsculas >> {}'.format(nome.lower()))
print('Quantas letras tem seu nome >> {}'.format(len(nome)))