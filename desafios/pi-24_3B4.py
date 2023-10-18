
# CODE:14
# IMPORTANTE: NO borrar los comentarios

cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3

numero_1 = int(input('Ingrese por favor un numero entero en la consola:\n'))

numero_2 = int(input('Ingrese por favor un numero entero distinto en la consola:\n'))

numero_3 = int(input('Ingrese por favor un ultimo numero entero en la consola:\n'))

# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.

if numero_1 > 0:
    cantidad_numeros_positivos += 1
    if numero_2 > 0:
        cantidad_numeros_positivos += 1
        if numero_3 > 0:
            cantidad_numeros_positivos +=1
        else:
            print(f'{numero_3} no es positivo')
    else:
        if numero_3 > 0:
            cantidad_numeros_positivos += 1
            print(f'{numero_2} no es positivo')
        else:
            print(f'{numero_3} no es positivo')
else:
    print(f'{numero_1} es menor o igual a 0')
    if numero_2 > 0:
        cantidad_numeros_positivos += 1
        if numero_3 > 0:
            cantidad_numeros_positivos += 1
        else:
            if numero_3 > 0:
                cantidad_numeros_positivos += 1
            else:
                print(f'{numero_3} es menor o igual a 0')
    else: 
        print(f'{numero_2} no es positivo')
        if numero_3 > 0:
            cantidad_numeros_positivos += 1
        else:
            print(f'{numero_3} es menor o igual a 0')


    


# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"

print(f'En esta trinidad, se contabilizan {cantidad_numeros_positivos} numeros positivos')

# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos
