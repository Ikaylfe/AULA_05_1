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

        
