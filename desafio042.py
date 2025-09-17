seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 == seg2 and seg2 == seg3:
    print(f'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif seg1 == seg2 and seg2 != seg3 or seg2 == seg3 and seg3 != seg1 or seg3 == seg1 and seg3 != seg2:
    print('Os segmentos PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos PODEM FORMAR um triângulo ESCALENO!')