nome = str(input('Qual é o seu nome? ')).lower().strip()
if nome == 'dhiogo':
    print('Belo nome!')
elif nome in 'sofia camily larissa julia juliana gabriela isabela':
    print('Belo nome feminino!')
else:
    print('Até que seu nome é bonito.')
print(f'Tenha um ótimo dia, {nome}!')