vet = []
for i in range(0, 10, 1):
    vet.append(int(input('Informe um valor: ')))

for i in range(0, 10, 1):
    if(vet[i] %2 == 0):
        vet[i] = 1
    else:
        vet[i] = 0

print(vet)  