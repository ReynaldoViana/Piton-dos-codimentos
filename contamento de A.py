nome = str(input('Digite sua frase:')).upper()
print('A apareceu: {}'.format(nome.count('A')))
print('A posição de first A é: {}'.format(nome.find('A')+1))
print('A ultima posição de A é: {}'.format(nome.rfind('A')+1))