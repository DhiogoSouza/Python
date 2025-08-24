from math import sqrt, ceil, floor
n = int(input('Digite um número para saber sua raiz quadrada: '))
raiz = sqrt(n)
print(f'A raiz quadrada de {n} é: {raiz:.2f}')
print(f'Arredondado pra cima é {ceil(raiz)}')
print(f'Arredondado pra baixo é {floor(raiz)}')

