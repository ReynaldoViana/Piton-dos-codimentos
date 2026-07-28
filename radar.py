vel = float(input('Digite sua velocidade:'))
multa = (vel -80) *7
if vel > 80:
    print('Você será multado em: {}'.format(multa))
else:
    print('Esta nas normas meu jovem!')