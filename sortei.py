import random
n1 =str(input('digite aluno 1'))
n2 =str(input('digite aluno 2'))
n3 =str(input('digite aluno 3'))
lista = [n1, n2, n3]
iscoido= random.choice(lista)
print('O aluno escolhido foi {}'.format(iscoido))