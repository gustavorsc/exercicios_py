def descubraMenor(val1, val2):
    if(val1 < val2):
        return (' {} é menor que {}'.format(val1, val2))
    elif(val2 < val1):
        return (' {} é menor que {}'.format(val2, val1))
    elif(val1 == val2):
        return (' {} é igual a {}'.format(val1, val2))
    
v1 = int(input('Informe um valor: '))
v2 = int(input('Informe um valor: '))
valor = descubraMenor(v1, v2)
print(valor)