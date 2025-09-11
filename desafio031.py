d = int(input('Qual a distância da sua viagem? '))
preco1 = d * 0.50
preco2 = d * 0.45
if d <= 200:
    print(f'O preço para sua viagem de {d}Km é de R${preco1:.2f}')
else:
    print(f'O preço para sua viagem de {d}Km é de R${preco2:.2f}')