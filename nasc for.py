from datetime import date
atual= date.today()
totalmaior = 0
totalmenor=0
for c in range(1, 8):
    nasc = int(input('Que ano nasceu{}?:'.format(c)))
    nas = atual.year - nasc
    if nas >=18:
        totalmaior+=1
    else:
        totalmenor+=1
print('Tiverão ao total maior de idade {} e {} menor de idade'.format(totalmaior,totalmenor))