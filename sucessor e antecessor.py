import math
n1 = int(input('Digite um valor:'))
suce= n1 + 1
ante = n1- 1
print('O sucessor será:', suce, ', O antecessor será:', ante)
dobro = n1*2
triplo = n1 *3
raiz = math.sqrt(n1)
print('O dobro será:', dobro, 'O triplo será:', triplo, 'A raiz será:', raiz)
n11 = int(input('Digite um valor'))
n2= int(input('Digite um valor'))
media = (n11+n2)/2
if media >=7:
    print('Aluno aprovado')
elif media >= 4:
    print('Aluno recuperação')
if media <4:
    print('Aluno reprovado')
print('A sua média será:', media)
metro = int(input('Digite seu Metro AI DENTRO'))
cm = metro * 100
mili = metro * 1000
print('O centimetro é:', cm, 'O milimetro será:', mili)
Conver = float(input('Qual valor você deseja converter em dolar'))
dolar = (Conver / 3.27)
print('Voce terá em Dólares:',dolar)
larg = int(input('Digite sua largura AIDENTO'))
compri= int(input('Digite seu comprimento AIDENTO'))
areia = larg * compri
tinta = (areia) / 2
print('O pintamento necessario de tinta será:', tinta)
n12 = int(input('Digite um valor'))
descont = n12 *(5/100)
Desconto= n12 - descont
print('O descotamento será:', descont)
print('O valor com descontamento será', Desconto)
sal = int(input('Digite seu salário'))
au = sal * (15/100)
aument = sal + au
print('O aumentamento será:', au)
print('Com aumentamento será', aument)