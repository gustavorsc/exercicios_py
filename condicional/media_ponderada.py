nome = str(input('Informe o nome do aluno: '))
nota_a = float(input('Informe a nota da prova A: '))
nota_b = float(input('Informe a nota da prova B: '))
media = ((nota_a *2 + nota_b)/3)
print('A média do aluno {} é de: {}.'.format(nome, media))