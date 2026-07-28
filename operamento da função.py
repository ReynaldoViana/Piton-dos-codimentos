n1 = int(input('digite valor:'))
n2 = int(input('Digite valor'))
soma = n1 + n2
prod = n1 * n2
if n2 == 0:
    print("Divisão inválida")
else:
    divi = n1 / n2
    divinteira = n1 // n2
resto = n1%n2
poten= pow(n1, n2)
print('A soma será:', soma, 'produto será:', prod, 'A divisão', divi, 'O resto será', resto, 'A potencia será:', poten)