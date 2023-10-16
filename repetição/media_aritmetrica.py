soma = 0
cont = 0
div = 0
while(cont < 10):
    n = int(input('Informe um número: '))
    if(n%2 == 0):
        soma += n
        div += 1
    cont += 1

media = soma / div
print('a média aritmetrica é de : {}'.format(media))