soma = 0
for n in range(0, 501, 1):
    if(n%3 == 0):
        if(n%2 != 0):
            soma += n

print('A soma dos multiplos de 3 entre 1 e 500 é de {}'.format(soma))