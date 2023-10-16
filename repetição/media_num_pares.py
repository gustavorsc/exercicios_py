soma = 0
cont = 0
num = 1
while(num != 0):
    num = int(input('Informe o numero: '))
    if(num%2 == 0):
        soma += num
        cont += 1
media = soma/cont
print('A media dos numeros pares é {}'.format(media))