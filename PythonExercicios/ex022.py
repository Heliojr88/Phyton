#Crie um o programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letra ao todo ( sem considerar espaços )
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo com as letras MAIÚSCULAS >> {}'.format(nome.upper()))
print('Seu nome com letras minúsculas >> {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} tem {} letras'.format(nome, nome.find(' ')))