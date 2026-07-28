l1 = float(input('Digite lado do triangulo'))
l2 = float(input('Digite lado do triangulo'))
l3 = float(input('Digite lado do triangulo'))
if l1 == l2 and l1 == l3 and l3 ==l2:
    print('Triangulo equilatero')
elif l1 == l2 or l1 == l3 or l3 ==l2:
    print('Tiangulo isosceles')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('triangulo escaleno')