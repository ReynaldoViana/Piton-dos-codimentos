num = int(input('digite seu numero'))
u = num // 1 %10
d = num // 10 %10
c = num // 100 %10
m = num//1000 %10
print('A unidade será:{}'.format(u))
print('A dezena será:{}'.format(d))
print('A centena será:{}'.format(c))
print('A milhar será:{}'.format(m))
