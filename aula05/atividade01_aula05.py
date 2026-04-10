print("""
[1] Sul 
[2] Norte 
[3] Leste 
[4] Oeste 
[5 a 6] Nordeste 
[7 a 9] Sudeste 
[10]Centro-Oeste 
[11] Noroeste
""")

codigo_produto=int(input('Informe o código do produto: '))

match codigo_produto:
    case 1:
        print('Produto produzido no Sul')
    case 2:
        print('Produto produzido no Norte')
    case 3:
        print('Produto produzido no Leste')
    case 4:
        print('Produto produzido no Oeste')
    case 5|6:
        print('Produto produzido no Nordeste')
    case 7|8|9:
        print('Produto produzido no Sudeste')
    case 10:
        print('Produto produzido no Centro-Oeste')
    case 11:
        print('Produto produzido no Noroeste')
    case _:
        print('Produto Importado')

