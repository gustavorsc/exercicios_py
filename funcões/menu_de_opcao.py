def resultado(num):
    if(num >= 1 and num <= 9):
        for i in range (1, 11, 1):
            print('{} x {} = {}'.format(i, num, i*num))

def imc():
    peso = float(input('Informe seu peso: '))
    h = float(input('Informe sua altura em metros EX: 1.77: '))
    imc = (peso/(h*h))
    print('O seu IMC é de {:.2f}'.format(imc))

def fatorial(num):
    fatorial = 1
    for i in range(1, num+1, 1):
        fatorial = fatorial * i
    print('O fatorial o número {} é {}'.format(num, fatorial))

op = int(input('Informe a opção desejada \n 1)Tabuada entre 1 e 9 \n 2)Calcular IMC \n 3)Calcular fatorial \n -1)sair do programa \n '))
while(op != -1):

    def switch(op):
        if(op == 1):
            num = int(input('Informe um numero: '))
            resultado(num)
        elif(op == 2):
            imc()
        elif(op == 3):
            num = int(input('Informe um numero: '))
            fatorial(num)
        elif(op == -1):
            print('Programa finalizado')

    op = int(input('Informe a opção desejada \n 1)Tabuada entre 1 e 9 \n 2)Calcular IMC \n 3)Calcular fatorial \n -1)sair do programa \n '))

    switch(op)