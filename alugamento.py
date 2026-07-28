dia= int(input('Quantos dias você quer alugar?'))
aludia = dia * 60
km= int(input('Quantos km você rodou?'))
kilo = km * 0.15
total = aludia + kilo
print('O total a ser pago será:{}'.format(total))