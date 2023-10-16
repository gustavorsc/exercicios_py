sexo = str(input('Informe o sexo sendo F para feminino e M para masculino: ')).upper()
h = float(input('Informe sua altura utilizando em metros: '))
if(sexo == 'M'):
    peso_ideal = (72.7 * h) - 58
    print('O seu peso ideal é de {}'.format(peso_ideal))
if(sexo == 'F'):
    peso_ideal = (62.1 * h) - 44.7
    print('O seu peso ideal é de {}'.format(peso_ideal))