a = input('Digite algo: ')
print('Informações sobre o que digitou abaixo: ')
print('======================================')
print(f'O tipo primitivo é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')
print('======================================')
print('Programa finalizado!')




