valor = float(input('Qual valor final da compra?'))
print('Método de pagamento?')
print('[1] A vista')
print('[2] Credito A vista')
print('[3] Parcelas em 2x')
print('[4] Parcelas em 3x ou mais' "Com Acrescimo")
op = int(input('Qual a opcao?'))
if op == 1:
    sim = valor - (valor * 0.10)
    print('O valor final ficará {}'.format(sim))
elif op ==2:
    op = valor - (valor * 0.05)
    print('NO crédito avista ficará: {}'.format(op))
elif op ==3:
    lp = valor / 2
    print('As parcelas em 2x ficará: {}'.format(lp))
elif op ==4:
    nop = valor + (valor * 0.20)
    print("A partir de 3 valor final ficará: {}".format(nop))