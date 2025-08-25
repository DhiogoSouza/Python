from math import hypot
cat_o = float(input('Informe o comprimento do cateto oposto: '))
cat_a = float(input('Informe o comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(cat_a, cat_o):.2f}')


