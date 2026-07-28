from datetime import date
ano = date.today().year
nas = int(input('Qual o ano de nascimento? '))
ida = ano - nas
if ida == 18:

    print('Bora se alistar meu patrão')

elif ida > 18:
    pinga = ida - 18
    print('Tu quer ser preso fih de égua, era pra se a alistar a {} anos'.format(pinga))
elif ida < 18:
    pitu = 18 - ida
    print('Tá ansioso demais, falta exatamente {} anos ainda'.format(pitu))