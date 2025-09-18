# Dicas de como simplificar com ajuda da IA
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)

# 1. A gente imprime o valor do IMC aqui, uma única vez.
print(f'Seu IMC é: {imc:.1f}')

# 2. Agora, a estrutura condicional se preocupa APENAS com a mensagem de status.
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
else: # A cima de 40
    print('Você está com obesidade mórbida.')




# Como eu fiz sozinho
'''peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'Seu IMC é: {imc:.1f}')
    print('Você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é: {imc:.1f}')
    print('Você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é: {imc:.1f}')
    print('Você está com sobrepeso')
elif imc <=40:
    print(f'Seu IMC é: {imc:.1f}')
    print('Você está com obesidade')
else:
    print(f'Seu IMC é: {imc:.1f}')
    print('Você está com obesidade mórbida.')'''






