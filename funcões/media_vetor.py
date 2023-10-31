def soma_vetor(vet):
    soma = 0
    for i in range(0, len(vet), 1):
        soma += vet[i]
    return soma

def media_vetor(vet, vet_tamanho):
   
    media = soma_vetor(vet)/vet_tamanho
    return media


vet = []
vet_tamanho = int(input('Informe o tamanho do vetor: '))
random = 0
for i in range (0, vet_tamanho, 1):
    vet.append(int(input('Informe um numero: ')))

soma = soma_vetor(vet)
media = media_vetor(vet, vet_tamanho)
print('A soma do vetor é de {}'.format(soma))
print('A media do vetor é de {}'.format(media))