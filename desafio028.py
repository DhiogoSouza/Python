from random import randint
from time import sleep

print('='*100)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('='*100)

n = int(input('Em que número eu pensei? '))
c = randint(0,5)
print('PROCESSANDO...')
sleep(1)
if n == c:
    print('Você venceu!!!')
else:
    print(f'VOCÊ PERDEU!!! Eu pensei no número {c}')


