# Valida números

numero= float(input('Insira um número:'))
match numero:
    case numero if numero < 0:
        print('Número negativo')
    case numero if numero > 0:
        print('Número positivo')
    case _:
        print('Neutro')


        
   