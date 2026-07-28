maior = 0
menor =0
for peso in range(1, 6):
    pesu = float(input('Qual o seu peso{}º?:'.format(peso)))
    if peso ==1:
        maior = pesu
        menor = pesu
    else:
        if peso > maior:
            maior = pesu
        if peso < menor:
            menor = pesu
print('o maior peso foi {}Kg'.format(maior))
print('o menor peso será {}Kg'.format(menor))