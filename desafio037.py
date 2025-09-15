#variaveis e opções de escola pro usuario
num = int(input('Digite um número inteiro: '))
print('Escola uma das bases para converter:')
print('''[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
conversao = int(input('Sua opção: '))

#realizando conversão
if conversao == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num) [2:]}')
elif conversao == 2:
    print(f'{num} convertido em OCTAL é {oct(num) [2:]}')
else:
    print(f'{num} convertido em HEXADECIMAL é {hex(num) [2:]}')