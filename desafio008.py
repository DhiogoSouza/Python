d = float(input('Uma distância em metros: '))
print(f'A medida de {d}m corresponde a')
print(f'{d * 0.00100:.3f}km')
print(f'{d * 0.0100:.2f}hm')
print(f'{d * 0.100:.1f}dam')
print(f'{d * 10.0:.0f}dm')
print(f'{d * 100:.0f}cm')
print(f'{d * 1000:.0f}mm')

#1 km = 1000 m, então metros / 1000

#1 hm = 100 m, então metros / 100

# 1 dam = 10 m, então metros / 10

# 1 m = 10 dm, então metros * 10, etc.