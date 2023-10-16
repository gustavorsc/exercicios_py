num = int(input('Informe o número: '))
cent = int(num/100)
cent_resto = num%100
dezena = int(cent_resto/10)
unit = cent_resto%10

print('O número {} invertido é {}{}{}'.format(num, unit, dezena, cent))