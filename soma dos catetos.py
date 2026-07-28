import math
co = float(input('Cateto oposto'))
ca = float(input('Cateto adjacente'))
pitas = pow(co, 2)+ pow(ca, 2)
print('A hiponetusa será: {}'.format(math.sqrt(pitas)))