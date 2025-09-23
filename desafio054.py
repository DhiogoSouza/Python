from datetime import date
contMaior = 0
contMenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print(f'Ao todo tivemos {contMaior} pessoas maiores de idade.')
print(f'E também tivemos {contMenor} pessoas menores de idade.')