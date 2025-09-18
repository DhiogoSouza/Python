preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista (dinheiro ou pix)
[2] à vista no cartão de crédito ou débito
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito''')
escolha = int(input('Qual opção escolhe? '))

print(f'O preço das suas compras foi: {preco}')

if escolha == 1:
    print(f'Um desconto de 10% foi aplicado a sua compra. Você pagará R${preco - (preco * 10 / 100):.2f}')
elif escolha == 2:
    print(f'Um desconto de 5% foi aplicado a sua compra. Você pagará R${preco - (preco * 5 / 100):.2f}')
elif escolha == 3:
    print(f'Sua compra foi parcelada em 2x sem juros. O valor total a ser pago é R${preco:.2f}')
elif escolha == 4:
    print(f'Foi aplicado 20% de juros na sua compra. O valor total a ser pago será de R${preco + (preco * 20 / 100):.2f}')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')