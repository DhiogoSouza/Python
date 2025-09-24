from random import randint
computador = randint(0, 10)

print('='*100)
print('Olá, sou seu computador e acabei de pensar em um número.')
print('Consegue adivinhar qual?')
print('='*100)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Dê seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...Tente novamente.')
        elif jogador < computador:
            print('Mais...Tente novamente.')
print(f'Você acertou com {palpite} tentativas. Parabéns! ')
