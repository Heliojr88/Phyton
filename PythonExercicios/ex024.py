# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('Sua cidade começa com a palavra SANTO >> {} é {}'.format(cidade, cidade[:5].upper() == 'SANTO'))