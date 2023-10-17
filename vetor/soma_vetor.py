vet = []
num = int(input('Informe o tamanho do vetor: '))
soma = 0
for i in range(0, num, 1):
    vet.append(int(input('Informe o valor do vetor na posição {}: '.format(i+1))))

for i in range(0, num, 1):
    soma += vet[i]

print('A soma dos elementos no vetor é de {}. '.format(soma))