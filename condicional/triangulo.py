val1 = int(input('Informe um valor: '))
val2 = int(input('Informe um valor: '))
val3 = int(input('Informe um valor: '))

if(val1+val2 > val3 and val2+val3 > val1 and val1+val3 > val2):
    if(val1 == val2 == val3):
        print('O triangulo de lados {}, {}, {}, é equilareto'.format(val1,val2,val3))
    elif(val1 == val2 or val2 == val3 or val1 == val3):
        print('O triangulo de lados {}, {}, {}, é isoceles'.format(val1,val2,val3))
    else:
        print('O triangulo de lados {}, {}, {}, é escaleno'.format(val1,val2,val3))
else:
    print('Não existe um triangulo com os lados {}, {}, {}.'.format(val1,val2,val3))