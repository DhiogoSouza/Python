print('Gerador de PA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# termo vai receber o primeiro numero
termo = primeiro

# cont já comeca com 1 para mostrar 10 numeros
cont = 1

# loop de menor ou igual a 10
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao   # termo pulando de acordo com a razao
    cont += 1        # contando ate 10
print('FIM!')