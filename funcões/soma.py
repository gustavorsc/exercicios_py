soma = 0.0
n = int(input('Informe um numero: '))
for i in range(1, n+1, 1):
    soma += i/(i*i)
    
print('A soma é de {:.2f}'.format(soma))