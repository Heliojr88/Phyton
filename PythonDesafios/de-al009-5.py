# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
print(frase)
f = frase.upper()
print('Quantas vezes aparece a letra "A" >> {}'.format(f.count('A')))
print('A primeira posição que aparece a letra "a" é >> {}'.format(f.find('A')))
print('A última posição que aparece a letra "a" é >> {}'.format(f.find('A')))