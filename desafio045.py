from random import randint
items = ('Pedra', 'Papel', 'Tesoura')
print('''ESCOLA UMA OPÇÃO
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua escolha? '))
computador = randint(0,2)
print(f'O jogador escolheu {items[jogador]} e o computador {items[computador]}')
if jogador == computador:
    print('DEU EMPATE!!!')
elif jogador == 0 and computador == 2:
    print('JOGADOR GANHOU!!!')
elif jogador == 1 and computador == 0:
    print('JOGADOR GANHOU!!!')
elif jogador == 2 and computador == 1:
    print('JOGADOR GANHOU!!!')
else:
    print('COMPUTADOR GANHOU!!!')
