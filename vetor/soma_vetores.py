vet = []
vet2 = []
vet_soma = []
for i in range(0, 5, 1):
    vet.append(int(input('Informe o valor no vetor 1 na posição {}: '.format(i+1))))

for i in range(0, 5, 1):
    vet2.append(int(input('Informe o valor no vetor 2 na posição {}: '.format(i+1))))

for i in range(0, 5, 1):
    vet_soma.append(vet[i] + vet2[i])

print('Soma dos vetores: ')
print(vet_soma)

 
