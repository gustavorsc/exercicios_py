CPF = []
soma = 0
for i in range(0, 11, 1):
    CPF.append(int(input('Informe o CPF sem pontos ou traço: ')))

for i in range(0, 11, 1):
    soma += CPF[i]

dezena = int(soma/10)
unit = soma%10
print(dezena, unit)