resposta= 'S'
while resposta != 'N':
    venda=float(input('Insira o valor da venda: '))
    if venda >= 1000:
        desc = venda* 0.1 
        total= venda - desc
        print (total)
    #soma += vend
    resposta = input('Quer continuar?  [S/N] ').upper().strip()[0]