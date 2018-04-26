# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))
equilatero = (a == b) == (a == c) == (b == c)
isosceles = (a == b) == (a == c) and b != c
prin
"""
escaleno = a != b, a != c, b != c
triangulo = a < b + c and b < a + c and c < a + b
if triangulo == True and equilatero:
    print('equilátero')
elif triangulo == True and isosceles:
    print('isósceles')
elif triangulo == True and escaleno:
    print('escaleno')
else:
    print('Não pode formar um triângulo')
"""