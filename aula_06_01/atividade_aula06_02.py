
# resposta= 'S'
# while resposta != 'N':
#     venda=float(input('Insira o valor da venda: '))
#     if venda >= 1000:
#         desc = venda* 0.1 
#         total= venda - desc
#         print (total)
#     #soma += vend
#     resposta = input('Quer continuar?  [S/N] ').upper().strip()[0]
     

# correção atividade 
resposta = 'S'
while resposta != 'N':
    valor = float (input('Informe o valor:  '))

    if valor > 1000:
        desconto = valor * 0.1
        valor -= desconto
        print(f'O valor a pagar é:{valor} ')

    resposta = input('Quer continuar [S/N]?').upper()  
print('Programa encerrado!')  
        





