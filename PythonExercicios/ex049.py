# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR
num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))