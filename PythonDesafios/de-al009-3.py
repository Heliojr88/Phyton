# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Cidade o nome da sua cidade: '))
print('Sua cidade {} \nComeça com a palavra SANTO >> '.format(cidade), 'Santo' in cidade)