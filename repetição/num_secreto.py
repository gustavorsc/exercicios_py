num_secreto = int(input('Coloque o número: '))
tentativas = 0
chute = num_secreto - 1

while(chute != num_secreto):
    chute = int(input('Informe o chute: '))
    if(chute > num_secreto):
        print('O chute foi maior que o número secreto.')
    if(chute < num_secreto):
        print('O chute foi menor que o número secreto.')
    tentativas += 1

print('Parabens, voce adivinhou o número secreto em {} tentativas.'.format(tentativas))