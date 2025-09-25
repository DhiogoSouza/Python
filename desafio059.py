# variaveis e input's
from time import sleep

opcao = 0
soma = 0
mult = 0
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

# corpo do codigo
while opcao != 5:
    print('='*50)
    print(
    '''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual opção você escolhe? '))

# if para opcao somar
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} + {valor2} é {soma}')

# if para opcao multiplicar
    if opcao == 2:
        mult = valor1 * valor2
        print(f'A multiplicação entre {valor1} x {valor2} é {mult}')

# if para opcao de maior numero
    if opcao == 3:
        print(f'O maior número entre {valor1} e {valor2} é {max(valor1, valor2)}')

# if para opcao de adicionar novos numeros
    if opcao == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

# if para opção inválida
    if opcao < 1 or opcao > 5:   #tinha colocado so > 5, IA me ajudou nessa
        print('Opção inválida. Tente novamente!!!')

# else para opcao 5 finalizar o programa
else:
    print('Finalizando...')
    sleep(1)
    print('Programa finalizado com sucesso!')
