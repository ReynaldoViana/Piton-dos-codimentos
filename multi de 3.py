soma = 0
for sim in range(1, 501, 2):
    if sim % 3 == 0:
        print(sim)
        soma += sim
        print(soma)
