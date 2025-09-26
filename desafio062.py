print('Gerador de PA')
print('='*20)
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Programa finalizado com {total} termos mostrados.')


