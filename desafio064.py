n = soma = cont = 0
n = int(input('Digite um número [999 para parar] '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar] '))
    if n == 999:
        print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

