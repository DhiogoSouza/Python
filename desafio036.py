#variaveis
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))

#calculando a parcela, prestação e o limite
parcela = financiamento * 12
prestacao = casa / parcela
limite_prestacao = salario * 0.30

#mensagens pro usuario
print(f'Para pagar uma casa de R${casa:.0f} em {financiamento} anos a prestação será de {prestacao:.2f}')
if prestacao <= limite_prestacao:
    print('Empréstimo APROVADO!')
else:
    print(f'Empréstimo NEGADO! A prestação mensal excede 30% do seu salário. ')


