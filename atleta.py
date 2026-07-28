idade =(int (input('Digite sua idade')))
if idade <= 9:
    print('Atleta mirim')
elif idade >9 and idade <=14:
    print("Atleta infantil")
elif idade > 14 and idade <=19:
    print('Atleta junior')
elif idade >19 and idade <=25:
    print('Atleta senior')
elif idade >25:
    print("Atleta Master")
