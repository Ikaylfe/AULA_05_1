# Estrutura de repetição While

# Número até 10

n=1
soma=0
while n !=0:
    n = int(input('Digite um numero: '))
    soma += n
print(f'O total foi: {soma}')    


#exemplo 3

resposta= 'S'
soma=0
while resposta!= 'N':
    n= int(input('Informe um número: '))
    soma += n
    resposta = input('Quer continuar?  [S/N] ').upper().strip()[0] 
        # <.upper> desconsidera maisculo e minusculo
    # <strip()> quebra linha
    # [0] pega somente a primeira letra
print(f'O total foi: {soma}')    
