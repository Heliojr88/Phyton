# Escreva um programa qualquer que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#  conversão: 1 para binário - 2 para octal - 3 para hexadecimal
print('=*' * 20)
print('Conversão BINÁRIO, OCTAL E HEXADECIMAL')
print('=*' * 20)
numero = int(input('Digite seu telefone: '))
escolha = str(input('Qual conversão gostaria de ver o número do seu celular {} BINÁRIO, OCTAL, HEXADECIMAL ou TODAS: '.format(numero))).strip().upper()
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]
binario = bin(numero)[2:]
if escolha == 'BINÁRIO':
    print('Seu número em BINÁRIO é {}'.format(binario))
elif escolha == 'OCTAL':
    print('Seu número em OCTAL é {}'.format(octal))
elif escolha == 'HEXADECIMAL':
    print('Seu número em HEXADECIMAL é {}'.format(hexadecimal))
elif escolha == 'TODAS':
    print('Seu número em todas as conversões é BINÁRIO {} OCTAL {} e HEXADECIMAL {}'.format(binario, octal, hexadecimal))
else:
    print('Erro ----- TENTE NOVAMENTE')
print('Obrigado')




