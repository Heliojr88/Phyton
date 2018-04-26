# Crie um programa que leia uma frase qualquer e diga se ela e um palíndromo, desconsiderando os espaços
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).upper().strip()
espaços = frase.count(' ')

print(espaços)
