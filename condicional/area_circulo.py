import math

pi = math.pi
raio = int(input('Informe o valor do raio: '))
area = (pi * raio**2)

print('A area do circulo com o raio de {} é de: {:.2f}'.format(raio, area))