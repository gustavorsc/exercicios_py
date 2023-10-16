hora = 10
min = 60 
print('Contagem regressiva iniciada: 10:00')
for hora in range(9, -1, -1):
    for min in range( 59, -1, -1):
        print('Contagem regressiva: {}:{}.'.format(hora, min)) 