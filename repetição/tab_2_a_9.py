num = int(input('Informe o número que desaja a tabuada sendo -1 o finalizador: '))
resp = 0
while(num > -1):
    for n in range(1,11,1):
        resp = num*n
        print('{} x {} = {}'.format(num, n, resp))
    num = int(input('Informe o número que desaja a tabuada entre 2 e 9: '))