# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR
n1 = int(input('Digite um número: '))
for c in range(1, 11):
    tabuada = n1 * c
    print('{} x {} = {}'.format(n1, c, tabuada))
print('FIM')
