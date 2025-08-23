preco = float(input('Qual o preço do produto? R$'))
desc = preco - (preco * 5 / 100)
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai custar R${desc:.2f}')

