km0 = float(input('Viajrá quantos km:'))
km1 = km0 * 0.50
km2 = km0 * 0.45
if km0 <=200:
    print('O seu total será: {}'.format(km1))
else:
    print('O seu total será: {}'.format(km2))