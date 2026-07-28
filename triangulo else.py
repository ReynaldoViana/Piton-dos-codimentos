a = int(input('Digite lado do triangulo:'))
b = int(input('Digite lado do triangulo:'))
c = int(input('Digite lado do triangulo:'))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Forma-se um triângulo')
else:
    print('Não forma um triângulo')