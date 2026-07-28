a = float(input('Digite um numero:'))
b = float(input('Digite um numero:'))
c = float(input('Digite um numero:'))
if a>b and a>c:
    print('É o maior valor:{}'.format(a))
elif b>a and b>c:
    print('É o maior valor:{}'.format(b))
elif c>a and c>b:
    print('É o maior valor:{}'.format(c))
