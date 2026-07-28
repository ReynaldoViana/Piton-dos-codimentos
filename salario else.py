sal = float(input('Digite seu salário'))
sal1 = sal * 0.10
sal2 = sal * 0.15
sal3 = sal + sal2
sal4 = sal + sal1
if sal <= 1250:
    print('O salario será: {}'.format(sal3))
else:
    print('O salario será: {}'.format(sal4))