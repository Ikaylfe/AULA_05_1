codigo = int(input('Informe o código de acesso: '))

match codigo:
    case 1:
        print('Marketing')
    case 2:
        print('Financeiro')
    case 3 | 4 | 5:
        print("ADM")
    case 6 | 7 | 8 | 9:
        print('TI')
    case 10:
        print('Serviços Gerais')
    case _:
        print('Acesso Negado')