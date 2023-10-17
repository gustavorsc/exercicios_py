vet = []
num = int(input('Informe o tamanho do vetor: '))
soma = 0
cont = 0
for i in range(0, num, 1):
    vet.append(int(input('Informe a nota do aluno na posição {}: '.format(i+1))))

for i in range(0, num, 1):
    soma += vet[i]

soma /= num

for i in range(0, num, 1):
    if(vet[i] < soma):
        cont += 1

print('A média da sala é de {}, {} alunos ficaram abaixo da média. '.format(soma, cont))