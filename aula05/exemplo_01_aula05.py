# Match Case
# print("""
# [1] - Marketing
# [2] - Financeiro
# [3 a 5] - ADM
# [6 a 9] - TI
# [10] - Serviços Gerais
# """)

# codigo = int(input('Informe o código de acesso: '))

# match codigo:
#     case 1:
#         print('Marketing')
#     case 2:
#         print('Financeiro')
#     case 3 | 4 | 5:
#         print("ADM")
#     case 6 | 7 | 8 | 9:
#         print('TI')
#     case 10:
#         print('Serviços Gerais')
#     case _:
#         print('Acesso Negado')

# Verifica a faixa etária

# idade=int(input('Informe a sua idade: '))
# match idade:
#     case idade if 0 <= idade < 12:
#         print('Criança.')
#     case idade if 12<= idade < 18:
#         print('Adolescente.')
#     case idade if idade >=18:
#         print('Adulto')        
#     case _: 
#         print('Idade inválida.')

# Escolha forma pgto
valor=float(input('Insira o valor de venda: '))
print("""
ESCOLHA A FORMA DE PGTO
      
      1 - Pix       (12% de desconto)
      2 - Débito    (8%  de desconto)
      3 - Crédito   (5%  de desconto)
      4 - Dinheiro  (15% de desconto)
              
      """)
forma_pgto=int(input('Seleciona a forma de pgto:'))
desc=0
match forma_pgto:
    case 1:
        desc=valor*0.12
        print('\n--- Pgto Pix---') #\n- esta opção faz pular uma linha.
    case 2:
        desc=valor*0.08
        print('\n--- Pgto Débito---')
    case 3:
        desc=valor*0.05   
        print('\n--- Pgto Crédito---')
    case 4:
        desc=valor*0.15   
        print('\n--- Pgto Dinheiro---')
    case _:
        print('Opção inválida!')
if desc !=0:
    total_venda= valor- desc
    print(f'Valor: {valor}')
    print(f'Valor do desconto: {desc}')
    print(f'Valor com desconto: {total_venda}')
else:
    print('Revise a opção digitada.')

        



