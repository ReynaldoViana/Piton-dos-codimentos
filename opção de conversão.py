n1 = int(input('Digite um numero: '))
print('[1] Binario')
print('[2] Octal')
print('[3] hexadecimal')
op = int(input(('Em qual deseja trasnformar?')))
if op ==1:
    print('{} em binario será:{}'.format(n1, bin(n1)[2:]))
elif op ==2:
    print('{} em octal será:{}'.format(n1, oct(n1)[2:]))
elif op == 3:
    print('{} em hexadecimal será: {}'.format(n1, hex(n1)[2:]))