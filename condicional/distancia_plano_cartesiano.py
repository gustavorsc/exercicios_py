import math
valor_x1 = int(input('Informe o valor de X do ponto 1: '))
valor_y1 = int(input('Informe o valor de Y do ponto 1: '))
valor_x2 = int(input('Informe o valor de X do ponto 2: '))
valor_y2 = int(input('Informe o valor de Y do ponto 2: '))

distancia = math.sqrt((valor_x2-valor_x1)**2 + (valor_y2-valor_y1)**2)

print('A distancia entre os pontos ({},{}) ({},{}) é de {}.'.format(valor_x1, valor_y1, valor_x2, valor_y2, distancia))