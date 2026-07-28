casa = float(input('Qual valor da casa?'))
sal = float(input('Qual seu salário?'))
ano = int(input('Em quantos  deseja pagar'))
prest1 = casa / (ano*12)
sal1 = sal * 0.30
print(f'\nPara pagar uma casa de R$ {casa:.2f} em {ano} anos:')
print(f'A prestação será de R$ {prest1:.2f}')
print(f'O limite do seu salário é R$ {sal1:.2f}\n')
if prest1 > sal1:
    print('Vá capinar um lote liso')
else:
    print('Seja bem vindo')
