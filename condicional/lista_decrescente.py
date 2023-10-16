a = int(input('Informe um valor: '))
b = int(input('Informe um valor: '))
c = int(input('Informe um valor: '))

if(a > b > c):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(a,b,c))
elif(a > c > b):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(a,c,b))
elif(b > a > c):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(b,a,c))
elif(b > c > a):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(b,c,a))
elif(c > a > b):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(c,a,b))
elif(c > b > a):
    print('Os números na ordem decrescente são: {}, {}, {}'.format(c,b,a))