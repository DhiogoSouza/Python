'''
um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é
de 15%.
'''
salario = int(input('Qual o salário do funcionário? R$'))
superior = salario + (salario * 10 / 100)
inferior = salario + (salario * 15 / 100)
if salario > 1250:
    print(f'Quem ganhava R${salario} passa a ganhar {superior:.2f}')
if salario < 1250:
    print(f' Quem ganhava R${salario} passa a ganhar {inferior}')
if salario == 1250:
    print(f'Quem ganha R${salario} não receberá aumento!!!')

