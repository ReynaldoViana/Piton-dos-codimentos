num = int(input('Digite um numero'))
for i in range(1,num+1):
    if num % i ==0:
        print('\033[34m',end='')
    else:
        print('\033[m',end='')
    print(i,end='')
print('\033[m')