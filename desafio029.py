vel = float(input('Qual a velocidade atual do carro? '))
# OU (vel - 80) * 7
excesso = vel - 80
multa = excesso * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
elif vel == 80:
    print('Você está no limite permitido! Não ultrapasse!')
else:
    print('Você está abaixo do limite permitido de 80Km/h!')
print('Digija com segurança!')

