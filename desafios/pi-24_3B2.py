
# CODE:11
# IMPORTANTE: NO borrar los comentarios

texto_1 = str(input('Ingrese la primera palabra:\n'))
texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable o la cree con ese valor

# Compare las dos palabras y entre sí 
# utilizando if y else.
# - Si texto_1 es mayor (alfabéticamente) a texto_2, 
#   almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1

if texto_1 > texto_2:
    res_1 = 1
    print(f'{texto_1} es mayor a {texto_2}')
else: 
    print(f'{texto_1} es menor a {texto_2}')

    res_1 = 2

# Imprimir en pantalla la variable res_1

print(f'{res_1}')

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Utilice if, elif y else
# - Si texto_1 tiene más letras, almacenar 1 en res_2
# - Si texto_2 tiene más letras, almacenar 2 en res_2
# - Si tienen la misma cantidad de letras, almacenar 3 en res_2

if len(texto_1) > len(texto_2):
    res_2 = 1
    print(f'{texto_1} tiene más letras que {texto_2}')
elif len(texto_2) > len(texto_1): 
    res_2 = 2
    print(f'Parece que {texto_2} tiene más letras que {texto_1}' )
else:
    res_2 = 3
    print(f'{texto_1} y {texto_2} tienen la misma cantidad de letras')

# Imprimir en pantalla la variable res_2

print(f'{res_2}')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# - Si la primera letra de texto_1 es mayor,
#   almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3

if texto_1[0] > texto_2[0]:
    res_3 = 1
    print(f'La letra {texto_1[0]} es mayor que la letra {texto_2[0]}')
else:
    res_3 = 2
    print(f'parece que la letra {texto_2[0]} es mayor que la letra {texto_1[0]}')

# Imprimir en pantalla la variable res_3

print(f'{res_3}')
