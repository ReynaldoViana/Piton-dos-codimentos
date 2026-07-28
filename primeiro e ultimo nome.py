name = str(input('nome completo:'))
nome = name.split()
print('muito prazer seu {}'.format(nome[0]))
print('Por acaso seu ultimo nome é:{}'.format(nome[len(nome)-1]))