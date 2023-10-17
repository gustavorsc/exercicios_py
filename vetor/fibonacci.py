fibonacci = [1, 1]
N = int(input('Informe ate onde ira o fibonacci: '))
for i in range(2, N, 1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)