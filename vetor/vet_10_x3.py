vet = []
vet3x = []
for i in range(0, 10, 1):
    vet.append(int(input('Informe o valor no vetor na posição {}: '.format(i+1))))

for i in range(0, 10, 1):
    vet3x.append(int(vet[i]*3))

print('Vetor Inicial:')
print(vet)
print('Vetor 3x:')
print(vet3x)