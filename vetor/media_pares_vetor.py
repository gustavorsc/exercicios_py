vet = []
num = int(input('Informe o tamanho do vetor: '))
soma = 0
cont = 0
for i in range(0, num, 1):
    vet.append(int(input('Informe o valor do vetor na posição {}: '.format(i+1))))

for i in range(0, num, 1):
    if(vet[i]%2 == 0):
        soma += vet[i]
        cont += 1

soma /= cont

print('A soma dos elementos no vetor é de {}. '.format(soma))
