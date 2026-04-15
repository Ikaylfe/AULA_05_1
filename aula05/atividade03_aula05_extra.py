# ‘** ATIVIDADE 01 ** 
# O algoritmo recebe 4 notas de um estudante, calcular sua média e mostrar no final, se está Aprovado, Recuperação ou Reprovado, conforme abaixo:  
# Média maior ou igual a 7, emitir mensagem de aprovado;  
# Média entre 5 e 7, Recuperação;  
# Abaixo de 5, emitir mensagem de reprovação.


nota01= float(input('Insira nota 01 : '))
nota02= float(input('Insira nota 02 : '))
nota03= float(input('Insira nota 03 : '))
nota04= float(input('Insira nota 04 : '))

media= (nota01+nota02+nota03+nota04)/4
print(f'Média do aluno = {media}')


match media:
    case media if media >=7.0:
        print ('Aluno aprovado!')
    case media if media >=5 < 7:
        print ('Aluno em Recuperação!') 
    case _:
         print( 'Aluno reprovado!')

