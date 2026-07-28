peso = float(input('Qual é seu peso'))
alt = float(input('Qual a sua altura?'))
imc = peso/(alt **2)
if imc < 18.5:
    print('Está abaixo do peso, o seu imc é: {}'.format(imc))
elif imc >= 18.5 and imc <=25:
    print('Peso ideal, o seu imc é: {}'.format(imc))
elif imc >25 and imc <=30:
    print('sobrepreso, o seu imc é: {}'.format(imc))
elif imc > 30 and imc <=40:
    print('Obesidade , o seu imc é: {}'.format(imc))
else:
    print('Obesidade Morbida, o seu imc é: {}'.format(imc))