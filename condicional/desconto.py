combustivel = str(input('Informe o combustivel sendo A-álcool e G-gasolina: ')).upper()
litros = float(input('Informe quantos litros foram colocados: '))
if(combustivel == 'A'):
    if(litros <= 20.0):
        valor_a_pagar = (litros * 2.10)
        desconto = valor_a_pagar/100 * 3
        valor_a_pagar = valor_a_pagar-desconto
        print('Valor a ser pago: {:.2f}, desconto aplicado de {:.2f}.'.format(valor_a_pagar, desconto))
    else:
        valor_a_pagar = (litros * 2.10)
        desconto = valor_a_pagar/100 * 5
        valor_a_pagar = valor_a_pagar - desconto
        print('Valor a ser pago: {:.2f}, desconto aplicado de {:.2f}.'.format(valor_a_pagar, desconto))
elif(combustivel == 'G'):
    if(litros <= 20.0):
        valor_a_pagar = (litros * 3.30)
        desconto = valor_a_pagar/100 * 4
        valor_a_pagar = valor_a_pagar-desconto
        print('Valor a ser pago: {:.2f}, desconto aplicado de {:.2f}.'.format(valor_a_pagar, desconto))
    else:
        valor_a_pagar = (litros * 3.30)
        desconto = valor_a_pagar/100 * 6
        valor_a_pagar = valor_a_pagar - desconto
        print('Valor a ser pago: {:.2f}, desconto aplicado de {:.2f}.'.format(valor_a_pagar, desconto))
else:
    print('Simbolo informado incorretamente')