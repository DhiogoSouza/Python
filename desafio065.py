quant = media = soma = 0
maior = []
menor = []
resp = 'S'
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    maior.append(num)
    menor.append(num)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {max(maior)} e o menor valor foi {min(menor)}')
