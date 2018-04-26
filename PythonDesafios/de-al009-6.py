# Faça um programa qie leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Segundo: Souza

nome = str(input('Digite seu nome completo: ')).strip()
sobrenome = nome.split()
print('Nome >>> {}'.format(sobrenome[0]))
print('Sobrenome >>> {}'.format(sobrenome[-1]))