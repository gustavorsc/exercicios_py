qtde = 0
vinho = ''
vinho_tinto = 0
vinho_branco = 0
vinho_rose = 0
while(vinho != 'F'):
    vinho = str(input('Informe o tipo do vinho, sendo T para vinho Tinto, B para vinho Branco e R para vinho Rosê, utilize F para sair do programa: ').upper())
    if(vinho == 'T'):
        vinho_tinto += 1
        qtde += 1
    if(vinho == 'B'):
        vinho_branco += 1
        qtde += 1
    if(vinho == 'R'):
        vinho_rose += 1
        qtde += 1    

porcentagem = 0.0
porcentagem = (vinho_tinto/qtde) * 100
print(qtde)
print('A porcentagem de vinho tinto na adega é de {:.2f}%'.format(porcentagem))
porcentagem = (vinho_branco/qtde) * 100
print('A porcentagem de vinho tinto na adega é de {:.2f}%'.format(porcentagem))
porcentagem = (vinho_rose/qtde) * 100
print('A porcentagem de vinho tinto na adega é de {:.2f}%'.format(porcentagem))